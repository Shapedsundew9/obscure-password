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
_IDENTITY = (
    'gAAAAABhE8O_1IUtgy2CnaGg7hH3GmVAULBlRkpGxnSl3Kpm4HHygfDCcs1pqkMN'
    'Iyy482vB4dV81S62UaNXjaDcgBv7PEbtSBpt7GtVomXt_wnDpr5qq-ZlZsxeRfxD'
    'M633KszF3_wMZjzFE0zKClrrnoxJL1ri23w1mxhJO2lQS_ny-iTw_c3nVZUL-Crj'
)
_S_LEN = len(_SCHMOOSH)
_I_LEN = len(_IDENTITY)


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
    schmoosh = (_SCHMOOSH * (int(len(text) / _S_LEN) + 1))
    xor = b64encode(bytes((_s ^ _t for _s, _t in zip(schmoosh, bytes(text, 'utf-8'))))).decode('utf-8')
    marker = (_IDENTITY * (int(len(xor) / _I_LEN) + 1))
    return ''.join((i + x for i, x in zip(marker, xor)))


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
    _logger.debug(f'Unobscuring {otext[:min(8, tl)]}...')
    identity = (_IDENTITY * (int(tl / _I_LEN) + 1))
    if identity[:tl // 2] == otext[0:tl:2]:
        b64 = otext[1:tl:2]
        schmoosh = (_SCHMOOSH * (int(len(b64) / _S_LEN) + 1))
        return bytes((_s ^ _t for _s, _t in zip(schmoosh, b64decode(b64)))).decode('utf-8')
    return otext
