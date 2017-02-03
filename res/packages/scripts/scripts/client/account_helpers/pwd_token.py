# 2017.02.03 21:46:52 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/account_helpers/pwd_token.py
from constants import DEFAULT_LANGUAGE
import hashlib
__all__ = ['generate']

def _generateMd5Hash(pwd):
    md = hashlib.md5()
    md.update(pwd)
    return md.hexdigest()


_BY_LANG = {'cn': _generateMd5Hash,
 'vn': _generateMd5Hash}

def generate(pwd):
    return pwd


if DEFAULT_LANGUAGE in _BY_LANG:
    generate = _BY_LANG[DEFAULT_LANGUAGE]
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\account_helpers\pwd_token.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:46:52 St�edn� Evropa (b�n� �as)
