import unicodedata
import re

BANNED_HEX = ['0x2010', '0x2011', '0x2012', '0x2013', '0x2014', '0x2015']
BANNED_CHARS = ''.join(chr(int(h, 16)) for h in BANNED_HEX)
BANNED_RE = re.compile('[' + re.escape(BANNED_CHARS) + ']')

def safe_emit(buf: str) -> str:
    """
    Final output sink guard. Normalize, then block if banned characters appear.
    This is the last defense before any text reaches a user.
    """
    buf = unicodedata.normalize('NFKC', buf)
    if BANNED_RE.search(buf):
        raise RuntimeError('sink guard blocked noncompliant output')
    return buf
