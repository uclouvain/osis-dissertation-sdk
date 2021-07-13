# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_dissertation_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.dissertation_role_status_enum import DissertationRoleStatusEnum
from osis_dissertation_sdk.model.error import Error
from osis_dissertation_sdk.model.pagination import Pagination
from osis_dissertation_sdk.model.proposition_dissertation_author import PropositionDissertationAuthor
from osis_dissertation_sdk.model.proposition_dissertation_detail import PropositionDissertationDetail
from osis_dissertation_sdk.model.proposition_dissertation_jury import PropositionDissertationJury
from osis_dissertation_sdk.model.proposition_dissertation_link import PropositionDissertationLink
from osis_dissertation_sdk.model.proposition_dissertation_row import PropositionDissertationRow
