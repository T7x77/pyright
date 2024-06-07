from _typeshed import Incomplete
from typing import Final

from reportlab.lib.rl_accel import unicode2T1 as unicode2T1

__version__: Final[str]
standardFonts: Incomplete
standardEncodings: Incomplete

class FontError(Exception): ...
class FontNotFoundError(Exception): ...

def parseAFMFile(afmFileName): ...

class TypeFace:
    name: Incomplete
    glyphNames: Incomplete
    glyphWidths: Incomplete
    ascent: int
    descent: int
    familyName: Incomplete
    bold: int
    italic: int
    requiredEncoding: str
    builtIn: int
    def __init__(self, name) -> None: ...
    def getFontFiles(self): ...
    def findT1File(self, ext: str = ".pfb"): ...

def bruteForceSearchForFile(fn, searchPath: Incomplete | None = None): ...
def bruteForceSearchForAFM(faceName): ...

class Encoding:
    name: Incomplete
    frozen: int
    baseEncodingName: Incomplete
    vector: Incomplete
    def __init__(self, name, base: Incomplete | None = None) -> None: ...
    def __getitem__(self, index): ...
    def __setitem__(self, index, value) -> None: ...
    def freeze(self) -> None: ...
    def isEqual(self, other): ...
    def modifyRange(self, base, newNames) -> None: ...
    def getDifferences(self, otherEnc): ...
    def makePDFObject(self): ...

standardT1SubstitutionFonts: Incomplete

class Font:
    fontName: Incomplete
    encoding: Incomplete
    encName: Incomplete
    substitutionFonts: Incomplete
    def __init__(self, name, faceName, encName, substitutionFonts: Incomplete | None = None) -> None: ...
    def stringWidth(self, text, size, encoding: str = "utf8"): ...
    def addObjects(self, doc) -> None: ...

PFB_MARKER: Incomplete
PFB_ASCII: Incomplete
PFB_BINARY: Incomplete
PFB_EOF: Incomplete

class EmbeddedType1Face(TypeFace):
    afmFileName: Incomplete
    pfbFileName: Incomplete
    requiredEncoding: Incomplete
    def __init__(self, afmFileName, pfbFileName) -> None: ...
    def getFontFiles(self): ...
    def addObjects(self, doc): ...

def registerTypeFace(face) -> None: ...
def registerEncoding(enc) -> None: ...
def registerFontFamily(
    family,
    normal: Incomplete | None = None,
    bold: Incomplete | None = None,
    italic: Incomplete | None = None,
    boldItalic: Incomplete | None = None,
) -> None: ...
def registerFont(font) -> None: ...
def getTypeFace(faceName): ...
def getEncoding(encName): ...
def findFontAndRegister(fontName): ...
def getFont(fontName): ...
def getAscentDescent(fontName, fontSize: Incomplete | None = None): ...
def getAscent(fontName, fontSize: Incomplete | None = None): ...
def getDescent(fontName, fontSize: Incomplete | None = None): ...
def getRegisteredFontNames(): ...
def stringWidth(text, fontName, fontSize, encoding: str = "utf8"): ...
def dumpFontData() -> None: ...
def test3widths(texts) -> None: ...
def testStringWidthAlgorithms() -> None: ...
def test() -> None: ...
