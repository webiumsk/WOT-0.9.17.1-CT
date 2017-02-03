# 2017.02.03 21:57:45 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/ctypes/test/test_buffers.py
from ctypes import *
import unittest

class StringBufferTestCase(unittest.TestCase):

    def test_buffer(self):
        b = create_string_buffer(32)
        self.assertEqual(len(b), 32)
        self.assertEqual(sizeof(b), 32 * sizeof(c_char))
        self.assertIs(type(b[0]), str)
        b = create_string_buffer('abc')
        self.assertEqual(len(b), 4)
        self.assertEqual(sizeof(b), 4 * sizeof(c_char))
        self.assertIs(type(b[0]), str)
        self.assertEqual(b[0], 'a')
        self.assertEqual(b[:], 'abc\x00')
        self.assertEqual(b[::], 'abc\x00')
        self.assertEqual(b[::-1], '\x00cba')
        self.assertEqual(b[::2], 'ac')
        self.assertEqual(b[::5], 'a')
        return

    def test_buffer_interface(self):
        self.assertEqual(len(bytearray(create_string_buffer(0))), 0)
        self.assertEqual(len(bytearray(create_string_buffer(1))), 1)

    def test_string_conversion(self):
        b = create_string_buffer(u'abc')
        self.assertEqual(len(b), 4)
        self.assertEqual(sizeof(b), 4 * sizeof(c_char))
        self.assertTrue(type(b[0]) is str)
        self.assertEqual(b[0], 'a')
        self.assertEqual(b[:], 'abc\x00')
        self.assertEqual(b[::], 'abc\x00')
        self.assertEqual(b[::-1], '\x00cba')
        self.assertEqual(b[::2], 'ac')
        self.assertEqual(b[::5], 'a')
        return

    try:
        c_wchar
    except NameError:
        pass
    else:

        def test_unicode_buffer(self):
            b = create_unicode_buffer(32)
            self.assertEqual(len(b), 32)
            self.assertEqual(sizeof(b), 32 * sizeof(c_wchar))
            self.assertIs(type(b[0]), unicode)
            b = create_unicode_buffer(u'abc')
            self.assertEqual(len(b), 4)
            self.assertEqual(sizeof(b), 4 * sizeof(c_wchar))
            self.assertIs(type(b[0]), unicode)
            self.assertEqual(b[0], u'a')
            self.assertEqual(b[:], 'abc\x00')
            self.assertEqual(b[::], 'abc\x00')
            self.assertEqual(b[::-1], '\x00cba')
            self.assertEqual(b[::2], 'ac')
            self.assertEqual(b[::5], 'a')
            return

        def test_unicode_conversion(self):
            b = create_unicode_buffer('abc')
            self.assertEqual(len(b), 4)
            self.assertEqual(sizeof(b), 4 * sizeof(c_wchar))
            self.assertIs(type(b[0]), unicode)
            self.assertEqual(b[0], u'a')
            self.assertEqual(b[:], 'abc\x00')
            self.assertEqual(b[::], 'abc\x00')
            self.assertEqual(b[::-1], '\x00cba')
            self.assertEqual(b[::2], 'ac')
            self.assertEqual(b[::5], 'a')
            return


if __name__ == '__main__':
    unittest.main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\ctypes\test\test_buffers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:57:45 St�edn� Evropa (b�n� �as)
