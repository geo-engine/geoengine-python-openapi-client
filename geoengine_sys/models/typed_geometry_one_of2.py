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



from pydantic import BaseModel, Field
from geoengine_sys.models.multi_line_string import MultiLineString

class TypedGeometryOneOf2(BaseModel):
    """
    TypedGeometryOneOf2
    """
    multi_line_string: MultiLineString = Field(..., alias="MultiLineString")
    __properties = ["MultiLineString"]

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
    def from_json(cls, json_str: str) -> TypedGeometryOneOf2:
        """Create an instance of TypedGeometryOneOf2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of multi_line_string
        if self.multi_line_string:
            _dict['MultiLineString'] = self.multi_line_string.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TypedGeometryOneOf2:
        """Create an instance of TypedGeometryOneOf2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TypedGeometryOneOf2.parse_obj(obj)

        _obj = TypedGeometryOneOf2.parse_obj({
            "multi_line_string": MultiLineString.from_dict(obj.get("MultiLineString")) if obj.get("MultiLineString") is not None else None
        })
        return _obj

