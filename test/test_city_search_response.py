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

from quedapi.models.city_search_response import CitySearchResponse  # noqa: E501

class TestCitySearchResponse(unittest.TestCase):
    """CitySearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CitySearchResponse:
        """Test CitySearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CitySearchResponse`
        """
        model = CitySearchResponse()  # noqa: E501
        if include_optional:
            return CitySearchResponse(
                city = quedapi.models.city.City(
                    territory_id = '', 
                    territory_name = '', 
                    state_code = '', 
                    publication_urls = [
                        ''
                        ], 
                    level = '', )
            )
        else:
            return CitySearchResponse(
                city = quedapi.models.city.City(
                    territory_id = '', 
                    territory_name = '', 
                    state_code = '', 
                    publication_urls = [
                        ''
                        ], 
                    level = '', ),
        )
        """

    def testCitySearchResponse(self):
        """Test CitySearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
