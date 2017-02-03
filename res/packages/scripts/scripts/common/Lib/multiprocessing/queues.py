# 2017.02.03 22:00:03 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/multiprocessing/queues.py
__all__ = ['Queue', 'SimpleQueue', 'JoinableQueue']
import sys
import os
import threading
import collections
import time
import atexit
import weakref
from Queue import Empty, Full
import _multiprocessing
from multiprocessing import Pipe
from multiprocessing.synchronize import Lock, BoundedSemaphore, Semaphore, Condition
from multiprocessing.util import debug, info, Finalize, register_after_fork
from multiprocessing.forking import assert_spawning

class Queue(object):

    def __init__(self, maxsize = 0):
        if maxsize <= 0:
            maxsize = _multiprocessing.SemLock.SEM_VALUE_MAX
        self._maxsize = maxsize
        self._reader, self._writer = Pipe(duplex=False)
        self._rlock = Lock()
        self._opid = os.getpid()
        if sys.platform == 'win32':
            self._wlock = None
        else:
            self._wlock = Lock()
        self._sem = BoundedSemaphore(maxsize)
        self._after_fork()
        if sys.platform != 'win32':
            register_after_fork(self, Queue._after_fork)
        return

    def __getstate__(self):
        assert_spawning(self)
        return (self._maxsize,
         self._reader,
         self._writer,
         self._rlock,
         self._wlock,
         self._sem,
         self._opid)

    def __setstate__(self, state):
        self._maxsize, self._reader, self._writer, self._rlock, self._wlock, self._sem, self._opid = state
        self._after_fork()

    def _after_fork(self):
        debug('Queue._after_fork()')
        self._notempty = threading.Condition(threading.Lock())
        self._buffer = collections.deque()
        self._thread = None
        self._jointhread = None
        self._joincancelled = False
        self._closed = False
        self._close = None
        self._send = self._writer.send
        self._recv = self._reader.recv
        self._poll = self._reader.poll
        return

    def put(self, obj, block = True, timeout = None):
        if not not self._closed:
            raise AssertionError
            raise self._sem.acquire(block, timeout) or Full
        self._notempty.acquire()
        try:
            if self._thread is None:
                self._start_thread()
            self._buffer.append(obj)
            self._notempty.notify()
        finally:
            self._notempty.release()

        return

    def get(self, block = True, timeout = None):
        if block and timeout is None:
            self._rlock.acquire()
            try:
                res = self._recv()
                self._sem.release()
                return res
            finally:
                self._rlock.release()

        else:
            if block:
                deadline = time.time() + timeout
            if not self._rlock.acquire(block, timeout):
                raise Empty
            try:
                if block:
                    timeout = deadline - time.time()
                    if timeout < 0 or not self._poll(timeout):
                        raise Empty
                elif not self._poll():
                    raise Empty
                res = self._recv()
                self._sem.release()
                return res
            finally:
                self._rlock.release()

        return

    def qsize(self):
        return self._maxsize - self._sem._semlock._get_value()

    def empty(self):
        return not self._poll()

    def full(self):
        return self._sem._semlock._is_zero()

    def get_nowait(self):
        return self.get(False)

    def put_nowait(self, obj):
        return self.put(obj, False)

    def close(self):
        self._closed = True
        self._reader.close()
        if self._close:
            self._close()

    def join_thread(self):
        debug('Queue.join_thread()')
        if not self._closed:
            raise AssertionError
            self._jointhread and self._jointhread()

    def cancel_join_thread(self):
        debug('Queue.cancel_join_thread()')
        self._joincancelled = True
        try:
            self._jointhread.cancel()
        except AttributeError:
            pass

    def _start_thread(self):
        debug('Queue._start_thread()')
        self._buffer.clear()
        self._thread = threading.Thread(target=Queue._feed, args=(self._buffer,
         self._notempty,
         self._send,
         self._wlock,
         self._writer.close), name='QueueFeederThread')
        self._thread.daemon = True
        debug('doing self._thread.start()')
        self._thread.start()
        debug('... done self._thread.start()')
        if not self._joincancelled:
            self._jointhread = Finalize(self._thread, Queue._finalize_join, [weakref.ref(self._thread)], exitpriority=-5)
        self._close = Finalize(self, Queue._finalize_close, [self._buffer, self._notempty], exitpriority=10)

    @staticmethod
    def _finalize_join(twr):
        debug('joining queue thread')
        thread = twr()
        if thread is not None:
            thread.join()
            debug('... queue thread joined')
        else:
            debug('... queue thread already dead')
        return

    @staticmethod
    def _finalize_close(buffer, notempty):
        debug('telling queue thread to quit')
        notempty.acquire()
        try:
            buffer.append(_sentinel)
            notempty.notify()
        finally:
            notempty.release()

    @staticmethod
    def _feed(buffer, notempty, send, writelock, close):
        debug('starting thread to feed data to pipe')
        from .util import is_exiting
        nacquire = notempty.acquire
        nrelease = notempty.release
        nwait = notempty.wait
        bpopleft = buffer.popleft
        sentinel = _sentinel
        if sys.platform != 'win32':
            wacquire = writelock.acquire
            wrelease = writelock.release
        else:
            wacquire = None
        try:
            while 1:
                nacquire()
                try:
                    if not buffer:
                        nwait()
                finally:
                    nrelease()

                try:
                    while 1:
                        obj = bpopleft()
                        if obj is sentinel:
                            debug('feeder thread got sentinel -- exiting')
                            close()
                            return
                        if wacquire is None:
                            send(obj)
                        else:
                            wacquire()
                            try:
                                send(obj)
                            finally:
                                wrelease()

                except IndexError:
                    pass

        except Exception as e:
            try:
                if is_exiting():
                    info('error in queue thread: %s', e)
                else:
                    import traceback
                    traceback.print_exc()
            except Exception:
                pass

        return


_sentinel = object()

class JoinableQueue(Queue):

    def __init__(self, maxsize = 0):
        Queue.__init__(self, maxsize)
        self._unfinished_tasks = Semaphore(0)
        self._cond = Condition()

    def __getstate__(self):
        return Queue.__getstate__(self) + (self._cond, self._unfinished_tasks)

    def __setstate__(self, state):
        Queue.__setstate__(self, state[:-2])
        self._cond, self._unfinished_tasks = state[-2:]

    def put(self, obj, block = True, timeout = None):
        if not not self._closed:
            raise AssertionError
            raise self._sem.acquire(block, timeout) or Full
        self._notempty.acquire()
        self._cond.acquire()
        try:
            if self._thread is None:
                self._start_thread()
            self._buffer.append(obj)
            self._unfinished_tasks.release()
            self._notempty.notify()
        finally:
            self._cond.release()
            self._notempty.release()

        return

    def task_done(self):
        self._cond.acquire()
        try:
            if not self._unfinished_tasks.acquire(False):
                raise ValueError('task_done() called too many times')
            if self._unfinished_tasks._semlock._is_zero():
                self._cond.notify_all()
        finally:
            self._cond.release()

    def join(self):
        self._cond.acquire()
        try:
            if not self._unfinished_tasks._semlock._is_zero():
                self._cond.wait()
        finally:
            self._cond.release()


class SimpleQueue(object):

    def __init__(self):
        self._reader, self._writer = Pipe(duplex=False)
        self._rlock = Lock()
        if sys.platform == 'win32':
            self._wlock = None
        else:
            self._wlock = Lock()
        self._make_methods()
        return

    def empty(self):
        return not self._reader.poll()

    def __getstate__(self):
        assert_spawning(self)
        return (self._reader,
         self._writer,
         self._rlock,
         self._wlock)

    def __setstate__(self, state):
        self._reader, self._writer, self._rlock, self._wlock = state
        self._make_methods()

    def _make_methods(self):
        recv = self._reader.recv
        racquire, rrelease = self._rlock.acquire, self._rlock.release

        def get():
            racquire()
            try:
                return recv()
            finally:
                rrelease()

        self.get = get
        if self._wlock is None:
            self.put = self._writer.send
        else:
            send = self._writer.send
            wacquire, wrelease = self._wlock.acquire, self._wlock.release

            def put(obj):
                wacquire()
                try:
                    return send(obj)
                finally:
                    wrelease()

            self.put = put
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\multiprocessing\queues.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 22:00:03 St�edn� Evropa (b�n� �as)