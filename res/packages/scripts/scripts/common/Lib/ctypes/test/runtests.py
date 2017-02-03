# 2017.02.03 21:57:44 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/ctypes/test/runtests.py
"""Usage: runtests.py [-q] [-r] [-v] [-u resources] [mask]

Run all tests found in this directory, and print a summary of the results.
Command line flags:
  -q     quiet mode: don't print anything while the tests are running
  -r     run tests repeatedly, look for refcount leaks
  -u<resources>
         Add resources to the lits of allowed resources. '*' allows all
         resources.
  -v     verbose mode: print the test currently executed
  -x<test1[,test2...]>
         Exclude specified tests.
  mask   mask to select filenames containing testcases, wildcards allowed
"""
import sys
import ctypes.test
if __name__ == '__main__':
    sys.exit(ctypes.test.main(ctypes.test))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\ctypes\test\runtests.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:57:44 St�edn� Evropa (b�n� �as)
