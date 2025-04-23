"""IWYouMyBrow"""

__title__ = "IWYouMyBrow"
__package__ = "IWYouMyBrow"
__autor__ = "GonzaTools"
__autor_email__ = "Gonzat1@protonmail.com"


  from  .__version__ import __version__
  from .checking import IWYouMyBrow as search
  from .IWYouMyBrow import main as cli
  from .sites import IWYouMyBrowEngine, IWYouMyBrowSites, IWYouMyBrowDatabase
from .notify import QueryNotifyPrint as Notifier