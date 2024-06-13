from ._parser import SiteParser

from .bouygues import BouyguesParser
from .danone import DanoneParser
from .dassault import DassaultParser
from .edf import EDFParser
from .expleo import ExpleoParser
from .indeed import IndeedParser
from .mbda import MBDAParser
from .orange import OrangeParser
from .safran import SafranParser
from .thales import ThalesParser

# List of all parsers
PARSERS = [
    ## Done

    # BouyguesParser,
    # DanoneParser,
    # DassaultParser,
    # EDFParser,
    # ExpleoParser,
    # IndeedParser,
    # MBDAParser,
    # OrangeParser,
    SafranParser,


    ## Doing
    
    ThalesParser,
    
    
    ## To do
    
]