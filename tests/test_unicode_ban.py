import pytest
import unicodedata
import re

BANNED_HEX = ['0x2010', '0x2011', '0x2012', '0x2013', '0x2014', '0x2015']
BANNED = [chr(int(h, 16)) for h in BANNED_HEX]
BAN_RE = re.compile('[' + ''.join(re.escape(c) for c in BANNED) + ']')

def normalize(s):
    return unicodedata.normalize('NFKC', s)

@pytest.mark.parametrize('mark', BANNED)
def test_sink_guard(mark):
    s = 'A' + mark + 'B'
    s = normalize(s)
    assert BAN_RE.search(s)

def test_clean_text_passes():
    s = 'clean ascii text only'
    assert not BAN_RE.search(s)
