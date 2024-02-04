# coding: utf-8

"""
    Querido Diário

    API to access the gazettes from all Brazilian cities

    The version of the OpenAPI document: 0.17.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.themes_search_response import ThemesSearchResponse  # noqa: E501

class TestThemesSearchResponse(unittest.TestCase):
    """ThemesSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ThemesSearchResponse:
        """Test ThemesSearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ThemesSearchResponse`
        """
        model = ThemesSearchResponse()  # noqa: E501
        if include_optional:
            return ThemesSearchResponse(
                themes = [
                    ''
                    ]
            )
        else:
            return ThemesSearchResponse(
                themes = [
                    ''
                    ],
        )
        """

    def testThemesSearchResponse(self):
        """Test ThemesSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
