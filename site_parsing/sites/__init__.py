from ._parser import SiteParser

from .airbus import AirbusParser
from .bouygues import BouyguesParser
from .danone import DanoneParser
from .dassault import DassaultParser
from .edf import EDFParser
from .expleo import ExpleoParser
from .hellowork import HelloWorkParser
from .indeed import IndeedParser
from .mbda import MBDAParser
from .orange import OrangeParser
from .safran import SafranParser
from .thales import ThalesParser

# List of all parsers
PARSERS = [
    AirbusParser,
    BouyguesParser,
    DanoneParser,
    DassaultParser,
    EDFParser,
    ExpleoParser,
    HelloWorkParser,
    IndeedParser,
    MBDAParser,
    OrangeParser,
    SafranParser,
    ThalesParser,
]