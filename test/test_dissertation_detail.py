"""
    Dissertation Service

    A set of API endpoints that allow you to get information about dissertation  # noqa: E501

    The version of the OpenAPI document: 1.00
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_dissertation_sdk
from osis_dissertation_sdk.model.defend_period_enum import DefendPeriodEnum
from osis_dissertation_sdk.model.dissertation_author import DissertationAuthor
from osis_dissertation_sdk.model.dissertation_jury import DissertationJury
from osis_dissertation_sdk.model.dissertation_link import DissertationLink
from osis_dissertation_sdk.model.dissertation_location import DissertationLocation
from osis_dissertation_sdk.model.dissertation_status_enum import DissertationStatusEnum
globals()['DefendPeriodEnum'] = DefendPeriodEnum
globals()['DissertationAuthor'] = DissertationAuthor
globals()['DissertationJury'] = DissertationJury
globals()['DissertationLink'] = DissertationLink
globals()['DissertationLocation'] = DissertationLocation
globals()['DissertationStatusEnum'] = DissertationStatusEnum
from osis_dissertation_sdk.model.dissertation_detail import DissertationDetail


class TestDissertationDetail(unittest.TestCase):
    """DissertationDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDissertationDetail(self):
        """Test DissertationDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DissertationDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()