# 2017.02.03 21:59:35 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_nonzero.py
"""Fixer for __nonzero__ -> __bool__ methods."""
from .. import fixer_base
from ..fixer_util import Name, syms

class FixNonzero(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    classdef< 'class' any+ ':'\n              suite< any*\n                     funcdef< 'def' name='__nonzero__'\n                              parameters< '(' NAME ')' > any+ >\n                     any* > >\n    "

    def transform(self, node, results):
        name = results['name']
        new = Name(u'__bool__', prefix=name.prefix)
        name.replace(new)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\fixes\fix_nonzero.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:59:35 St�edn� Evropa (b�n� �as)
