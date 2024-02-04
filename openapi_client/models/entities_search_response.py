# coding: utf-8

"""
    Querido Diário

    API to access the gazettes from all Brazilian cities

    The version of the OpenAPI document: 0.17.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from openapi_client.models.entity import Entity

class EntitiesSearchResponse(BaseModel):
    """
    EntitiesSearchResponse
    """
    entities: conlist(Entity) = Field(...)
    __properties = ["entities"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EntitiesSearchResponse:
        """Create an instance of EntitiesSearchResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item in self.entities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entities'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EntitiesSearchResponse:
        """Create an instance of EntitiesSearchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EntitiesSearchResponse.parse_obj(obj)

        _obj = EntitiesSearchResponse.parse_obj({
            "entities": [Entity.from_dict(_item) for _item in obj.get("entities")] if obj.get("entities") is not None else None
        })
        return _obj


