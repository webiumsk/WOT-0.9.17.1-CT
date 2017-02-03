# 2017.02.03 21:59:11 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/json/tests/test_separators.py
import textwrap
from json.tests import PyTest, CTest

class TestSeparators(object):

    def test_separators(self):
        h = [['blorpie'],
         ['whoops'],
         [],
         'd-shtaeou',
         'd-nthiouh',
         'i-vhbjkhnth',
         {'nifty': 87},
         {'field': 'yes',
          'morefield': False}]
        expect = textwrap.dedent('        [\n          [\n            "blorpie"\n          ] ,\n          [\n            "whoops"\n          ] ,\n          [] ,\n          "d-shtaeou" ,\n          "d-nthiouh" ,\n          "i-vhbjkhnth" ,\n          {\n            "nifty" : 87\n          } ,\n          {\n            "field" : "yes" ,\n            "morefield" : false\n          }\n        ]')
        d1 = self.dumps(h)
        d2 = self.dumps(h, indent=2, sort_keys=True, separators=(' ,', ' : '))
        h1 = self.loads(d1)
        h2 = self.loads(d2)
        self.assertEqual(h1, h)
        self.assertEqual(h2, h)
        self.assertEqual(d2, expect)


class TestPySeparators(TestSeparators, PyTest):
    pass


class TestCSeparators(TestSeparators, CTest):
    pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\json\tests\test_separators.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:59:11 St�edn� Evropa (b�n� �as)
