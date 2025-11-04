import unicodedata

BANNED_HEX = ['0x2010', '0x2011', '0x2012', '0x2013', '0x2014', '0x2015']
BANNED = {int(h, 16) for h in BANNED_HEX}

class PolicyViolation(Exception):
    """Raised when a banned codepoint is emitted."""
    pass

def on_token(token_text: str) -> str:
    """
    Token-level hook. Normalize, then scan for banned codepoints.
    Raise PolicyViolation on detection.
    """
    t = unicodedata.normalize('NFKC', token_text)
    for ch in t:
        if ord(ch) in BANNED:
            raise PolicyViolation('banned unicode dash detected')
    return t
