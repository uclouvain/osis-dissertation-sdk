"""
    Dissertation Service

    A set of API endpoints that allow you to get information about dissertation  # noqa: E501

    The version of the OpenAPI document: 1.01
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_dissertation_sdk
from osis_dissertation_sdk.api.adviser_api import AdviserApi  # noqa: E501


class TestAdviserApi(unittest.TestCase):
    """AdviserApi unit test stubs"""

    def setUp(self):
        self.api = AdviserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_advisers_list(self):
        """Test case for advisers_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
