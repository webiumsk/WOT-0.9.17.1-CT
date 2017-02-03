# 2017.02.03 21:59:07 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/idlelib/idle_test/test_pathbrowser.py
import unittest
import idlelib.PathBrowser as PathBrowser

class PathBrowserTest(unittest.TestCase):

    def test_DirBrowserTreeItem(self):
        d = PathBrowser.DirBrowserTreeItem('')
        d.GetSubList()


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\idlelib\idle_test\test_pathbrowser.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:59:07 Støední Evropa (bìžný èas)
