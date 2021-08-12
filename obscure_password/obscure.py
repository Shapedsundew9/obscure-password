"""Self contained obfuscation of hardcoded passwords in Python scripts."""
from base64 import b64decode, b64encode
from logging import NullHandler, getLogger

_logger = getLogger(__name__)
_logger.addHandler(NullHandler())


_SCHMOOSH = (
    b'Z0FBQUFBQmhFOFJTemI4MFRnU1ZuS0xLZHNtZzVfbUJDeE5RWTl0eFp4NWNabFJk'
    b'LRGgwMVJuNElab2hoUl9HazRaRWZXSURmNGduYjNiTzdGWVNFa2pzdk5IMGtMTn!'
    b'hiLWk4bjZXWFNhWGdzVFBBNG5VNWF0SEdZUVJDMXNBRmVONmVXdmQ0X29BaGk=&*'
)
_IDENTITY = b'_1IUtgy2CnaG'
_I_LEN = len(_IDENTITY)
_I_B64_LEN = (_I_LEN * 4 + 1) // 3


def _schmoosh_generator():
    while True:
        for s in _SCHMOOSH:
            yield s


def obscure(text):
    """Obscure text.

    Text is obscured and laced with a marker that unobscure() will detect.

    Args
    ----
    text(str): Text to obscure.

    Returns
    -------
    (str) Obscured text.
    """
    _logger.debug('Obscuring text ********')
    schmoosh = _schmoosh_generator()
    xor = b64encode(bytes((next(schmoosh) ^ bytes(t, 'utf-8')[0] for t in text))).decode('utf-8')
    filter = len(xor) & 0xFF
    marker = b64encode((bytes((i ^ filter for i in _IDENTITY)))).decode('utf-8')
    return marker + xor


def unobscure(otext):
    """Unobscure text obscured with obscure().

    If the marker placed in by obscure() cannot be detected otext is
    returned unmodified.

    Args
    ----
    text(str): Text obscured with obscure().

    Returns
    -------
    (str) Unobscured (orginal) text.
    """
    tl = len(otext)
    filter = (tl - _I_B64_LEN) & 0xFF
    marker = b64encode((bytes((i ^ filter for i in _IDENTITY)))).decode('utf-8')
    _logger.debug(f'Unobscuring {otext[:min(8, tl)]}...')
    if otext[:_I_B64_LEN] == marker:
        b64 = otext[_I_B64_LEN:]
        schmoosh = _schmoosh_generator()
        return bytes((next(schmoosh) ^ b for b in b64decode(b64))).decode('utf-8')
    return otext
