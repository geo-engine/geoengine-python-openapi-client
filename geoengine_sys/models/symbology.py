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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from geoengine_sys.models.line_symbology_with_type import LineSymbologyWithType
from geoengine_sys.models.point_symbology_with_type import PointSymbologyWithType
from geoengine_sys.models.polygon_symbology_with_type import PolygonSymbologyWithType
from geoengine_sys.models.raster_symbology_with_type import RasterSymbologyWithType
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

SYMBOLOGY_ONE_OF_SCHEMAS = ["LineSymbologyWithType", "PointSymbologyWithType", "PolygonSymbologyWithType", "RasterSymbologyWithType"]

class Symbology(BaseModel):
    """
    Symbology
    """
    # data type: RasterSymbologyWithType
    oneof_schema_1_validator: Optional[RasterSymbologyWithType] = None
    # data type: PointSymbologyWithType
    oneof_schema_2_validator: Optional[PointSymbologyWithType] = None
    # data type: LineSymbologyWithType
    oneof_schema_3_validator: Optional[LineSymbologyWithType] = None
    # data type: PolygonSymbologyWithType
    oneof_schema_4_validator: Optional[PolygonSymbologyWithType] = None
    if TYPE_CHECKING:
        actual_instance: Union[LineSymbologyWithType, PointSymbologyWithType, PolygonSymbologyWithType, RasterSymbologyWithType]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(SYMBOLOGY_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = Symbology.construct()
        error_messages = []
        match = 0
        # validate data type: RasterSymbologyWithType
        if not isinstance(v, RasterSymbologyWithType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RasterSymbologyWithType`")
        else:
            match += 1
        # validate data type: PointSymbologyWithType
        if not isinstance(v, PointSymbologyWithType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PointSymbologyWithType`")
        else:
            match += 1
        # validate data type: LineSymbologyWithType
        if not isinstance(v, LineSymbologyWithType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LineSymbologyWithType`")
        else:
            match += 1
        # validate data type: PolygonSymbologyWithType
        if not isinstance(v, PolygonSymbologyWithType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PolygonSymbologyWithType`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in Symbology with oneOf schemas: LineSymbologyWithType, PointSymbologyWithType, PolygonSymbologyWithType, RasterSymbologyWithType. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in Symbology with oneOf schemas: LineSymbologyWithType, PointSymbologyWithType, PolygonSymbologyWithType, RasterSymbologyWithType. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Symbology:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Symbology:
        """Returns the object represented by the json string"""
        instance = Symbology.construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `type` in the input.")

        # check if data type is `LineSymbologyWithType`
        if _data_type == "LineSymbologyWithType":
            instance.actual_instance = LineSymbologyWithType.from_json(json_str)
            return instance

        # check if data type is `PointSymbologyWithType`
        if _data_type == "PointSymbologyWithType":
            instance.actual_instance = PointSymbologyWithType.from_json(json_str)
            return instance

        # check if data type is `PolygonSymbologyWithType`
        if _data_type == "PolygonSymbologyWithType":
            instance.actual_instance = PolygonSymbologyWithType.from_json(json_str)
            return instance

        # check if data type is `RasterSymbologyWithType`
        if _data_type == "RasterSymbologyWithType":
            instance.actual_instance = RasterSymbologyWithType.from_json(json_str)
            return instance

        # check if data type is `LineSymbologyWithType`
        if _data_type == "line":
            instance.actual_instance = LineSymbologyWithType.from_json(json_str)
            return instance

        # check if data type is `PointSymbologyWithType`
        if _data_type == "point":
            instance.actual_instance = PointSymbologyWithType.from_json(json_str)
            return instance

        # check if data type is `PolygonSymbologyWithType`
        if _data_type == "polygon":
            instance.actual_instance = PolygonSymbologyWithType.from_json(json_str)
            return instance

        # check if data type is `RasterSymbologyWithType`
        if _data_type == "raster":
            instance.actual_instance = RasterSymbologyWithType.from_json(json_str)
            return instance

        # deserialize data into RasterSymbologyWithType
        try:
            instance.actual_instance = RasterSymbologyWithType.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PointSymbologyWithType
        try:
            instance.actual_instance = PointSymbologyWithType.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LineSymbologyWithType
        try:
            instance.actual_instance = LineSymbologyWithType.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PolygonSymbologyWithType
        try:
            instance.actual_instance = PolygonSymbologyWithType.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into Symbology with oneOf schemas: LineSymbologyWithType, PointSymbologyWithType, PolygonSymbologyWithType, RasterSymbologyWithType. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Symbology with oneOf schemas: LineSymbologyWithType, PointSymbologyWithType, PolygonSymbologyWithType, RasterSymbologyWithType. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

