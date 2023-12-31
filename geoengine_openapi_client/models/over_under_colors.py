# coding: utf-8

"""
    Geo Engine Pro API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.7.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist

class OverUnderColors(BaseModel):
    """
    OverUnderColors
    """
    over_color: conlist(StrictInt, max_items=4, min_items=4) = Field(..., alias="overColor")
    under_color: conlist(StrictInt, max_items=4, min_items=4) = Field(..., alias="underColor")
    __properties = ["overColor", "underColor"]

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
    def from_json(cls, json_str: str) -> OverUnderColors:
        """Create an instance of OverUnderColors from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OverUnderColors:
        """Create an instance of OverUnderColors from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OverUnderColors.parse_obj(obj)

        _obj = OverUnderColors.parse_obj({
            "over_color": obj.get("overColor"),
            "under_color": obj.get("underColor")
        })
        return _obj


