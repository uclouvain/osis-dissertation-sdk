
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.adviser_api import AdviserApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from osis_dissertation_sdk.api.adviser_api import AdviserApi
from osis_dissertation_sdk.api.dissertation_api import DissertationApi
from osis_dissertation_sdk.api.dissertation_location_api import DissertationLocationApi
from osis_dissertation_sdk.api.proposition_dissertation_api import PropositionDissertationApi
