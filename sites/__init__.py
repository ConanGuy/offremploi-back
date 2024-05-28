from ._parser import SiteParser

from .danone import DanoneParser
from .dassault import DassaultParser
from .edf import EDFParser
from .expleo import ExpleoParser
from .indeedIgny import IndeedIgnyParser
from .indeedElancourt import IndeedElancourtParser
from .mbda import MBDAParser
from .orange import OrangeParser
from .safran import SafranParser
from .thales import ThalesParser

# List of all parsers
PARSERS = [
    DanoneParser,
    DassaultParser,
    EDFParser,
    ExpleoParser,
    IndeedIgnyParser,
    IndeedElancourtParser,
    MBDAParser,
    OrangeParser,
    SafranParser,
    ThalesParser
]