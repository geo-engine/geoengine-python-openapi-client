# coding: utf-8

# flake8: noqa

"""
    Geo Engine Pro API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.7.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.1"

# import apis into sdk package
from geoengine_openapi_client.api.datasets_api import DatasetsApi
from geoengine_openapi_client.api.general_api import GeneralApi
from geoengine_openapi_client.api.layers_api import LayersApi
from geoengine_openapi_client.api.ogcwcs_api import OGCWCSApi
from geoengine_openapi_client.api.ogcwfs_api import OGCWFSApi
from geoengine_openapi_client.api.ogcwms_api import OGCWMSApi
from geoengine_openapi_client.api.permissions_api import PermissionsApi
from geoengine_openapi_client.api.projects_api import ProjectsApi
from geoengine_openapi_client.api.session_api import SessionApi
from geoengine_openapi_client.api.spatial_references_api import SpatialReferencesApi
from geoengine_openapi_client.api.tasks_api import TasksApi
from geoengine_openapi_client.api.uploads_api import UploadsApi
from geoengine_openapi_client.api.user_api import UserApi
from geoengine_openapi_client.api.workflows_api import WorkflowsApi

# import ApiClient
from geoengine_openapi_client.api_response import ApiResponse
from geoengine_openapi_client.api_client import ApiClient
from geoengine_openapi_client.configuration import Configuration
from geoengine_openapi_client.exceptions import OpenApiException
from geoengine_openapi_client.exceptions import ApiTypeError
from geoengine_openapi_client.exceptions import ApiValueError
from geoengine_openapi_client.exceptions import ApiKeyError
from geoengine_openapi_client.exceptions import ApiAttributeError
from geoengine_openapi_client.exceptions import ApiException

# import models into sdk package
from geoengine_openapi_client.models.aborted_task_status import AbortedTaskStatus
from geoengine_openapi_client.models.add_collection200_response import AddCollection200Response
from geoengine_openapi_client.models.add_dataset import AddDataset
from geoengine_openapi_client.models.add_layer import AddLayer
from geoengine_openapi_client.models.add_layer_collection import AddLayerCollection
from geoengine_openapi_client.models.add_role import AddRole
from geoengine_openapi_client.models.auto_create_dataset import AutoCreateDataset
from geoengine_openapi_client.models.auto_ogr_source_time_format import AutoOgrSourceTimeFormat
from geoengine_openapi_client.models.axis_order import AxisOrder
from geoengine_openapi_client.models.bounding_box2_d import BoundingBox2D
from geoengine_openapi_client.models.breakpoint import Breakpoint
from geoengine_openapi_client.models.classification_measurement import ClassificationMeasurement
from geoengine_openapi_client.models.classification_measurement_with_type import ClassificationMeasurementWithType
from geoengine_openapi_client.models.collection_item import CollectionItem
from geoengine_openapi_client.models.collection_type import CollectionType
from geoengine_openapi_client.models.color_param import ColorParam
from geoengine_openapi_client.models.colorizer import Colorizer
from geoengine_openapi_client.models.completed_task_status import CompletedTaskStatus
from geoengine_openapi_client.models.continuous_measurement import ContinuousMeasurement
from geoengine_openapi_client.models.continuous_measurement_with_type import ContinuousMeasurementWithType
from geoengine_openapi_client.models.coordinate2_d import Coordinate2D
from geoengine_openapi_client.models.create_dataset import CreateDataset
from geoengine_openapi_client.models.create_dataset_handler200_response import CreateDatasetHandler200Response
from geoengine_openapi_client.models.create_project import CreateProject
from geoengine_openapi_client.models.csv_header import CsvHeader
from geoengine_openapi_client.models.custom_ogr_source_time_format import CustomOgrSourceTimeFormat
from geoengine_openapi_client.models.data_id import DataId
from geoengine_openapi_client.models.data_path import DataPath
from geoengine_openapi_client.models.data_path_one_of import DataPathOneOf
from geoengine_openapi_client.models.data_path_one_of1 import DataPathOneOf1
from geoengine_openapi_client.models.dataset import Dataset
from geoengine_openapi_client.models.dataset_definition import DatasetDefinition
from geoengine_openapi_client.models.dataset_id_resource_id import DatasetIdResourceId
from geoengine_openapi_client.models.dataset_listing import DatasetListing
from geoengine_openapi_client.models.dataset_resource import DatasetResource
from geoengine_openapi_client.models.date_time import DateTime
from geoengine_openapi_client.models.date_time_parse_format import DateTimeParseFormat
from geoengine_openapi_client.models.default_colors import DefaultColors
from geoengine_openapi_client.models.default_colors_one_of import DefaultColorsOneOf
from geoengine_openapi_client.models.derived_color import DerivedColor
from geoengine_openapi_client.models.derived_color_with_type import DerivedColorWithType
from geoengine_openapi_client.models.derived_number import DerivedNumber
from geoengine_openapi_client.models.derived_number_with_type import DerivedNumberWithType
from geoengine_openapi_client.models.describe_coverage_request import DescribeCoverageRequest
from geoengine_openapi_client.models.error_response import ErrorResponse
from geoengine_openapi_client.models.external_data_id import ExternalDataId
from geoengine_openapi_client.models.external_data_id_with_type import ExternalDataIdWithType
from geoengine_openapi_client.models.failed_task_status import FailedTaskStatus
from geoengine_openapi_client.models.feature_data_type import FeatureDataType
from geoengine_openapi_client.models.file_not_found_handling import FileNotFoundHandling
from geoengine_openapi_client.models.format_specifics import FormatSpecifics
from geoengine_openapi_client.models.format_specifics_one_of import FormatSpecificsOneOf
from geoengine_openapi_client.models.format_specifics_one_of_csv import FormatSpecificsOneOfCsv
from geoengine_openapi_client.models.gdal_dataset_geo_transform import GdalDatasetGeoTransform
from geoengine_openapi_client.models.gdal_dataset_parameters import GdalDatasetParameters
from geoengine_openapi_client.models.gdal_loading_info_temporal_slice import GdalLoadingInfoTemporalSlice
from geoengine_openapi_client.models.gdal_meta_data_list import GdalMetaDataList
from geoengine_openapi_client.models.gdal_meta_data_list_with_type import GdalMetaDataListWithType
from geoengine_openapi_client.models.gdal_meta_data_regular import GdalMetaDataRegular
from geoengine_openapi_client.models.gdal_meta_data_regular_with_type import GdalMetaDataRegularWithType
from geoengine_openapi_client.models.gdal_meta_data_static import GdalMetaDataStatic
from geoengine_openapi_client.models.gdal_meta_data_static_with_type import GdalMetaDataStaticWithType
from geoengine_openapi_client.models.gdal_metadata_mapping import GdalMetadataMapping
from geoengine_openapi_client.models.gdal_metadata_net_cdf_cf import GdalMetadataNetCdfCf
from geoengine_openapi_client.models.gdal_metadata_net_cdf_cf_with_type import GdalMetadataNetCdfCfWithType
from geoengine_openapi_client.models.gdal_source_time_placeholder import GdalSourceTimePlaceholder
from geoengine_openapi_client.models.geo_json import GeoJson
from geoengine_openapi_client.models.get_capabilities_format import GetCapabilitiesFormat
from geoengine_openapi_client.models.get_capabilities_request import GetCapabilitiesRequest
from geoengine_openapi_client.models.get_coverage_format import GetCoverageFormat
from geoengine_openapi_client.models.get_coverage_request import GetCoverageRequest
from geoengine_openapi_client.models.get_feature_request import GetFeatureRequest
from geoengine_openapi_client.models.get_legend_graphic_request import GetLegendGraphicRequest
from geoengine_openapi_client.models.get_map_exception_format import GetMapExceptionFormat
from geoengine_openapi_client.models.get_map_format import GetMapFormat
from geoengine_openapi_client.models.get_map_request import GetMapRequest
from geoengine_openapi_client.models.infinite_ogr_source_duration_spec import InfiniteOgrSourceDurationSpec
from geoengine_openapi_client.models.internal_data_id import InternalDataId
from geoengine_openapi_client.models.layer import Layer
from geoengine_openapi_client.models.layer_collection import LayerCollection
from geoengine_openapi_client.models.layer_collection_listing import LayerCollectionListing
from geoengine_openapi_client.models.layer_collection_listing_with_type import LayerCollectionListingWithType
from geoengine_openapi_client.models.layer_collection_resource import LayerCollectionResource
from geoengine_openapi_client.models.layer_collection_resource_id import LayerCollectionResourceId
from geoengine_openapi_client.models.layer_listing import LayerListing
from geoengine_openapi_client.models.layer_listing_with_type import LayerListingWithType
from geoengine_openapi_client.models.layer_resource import LayerResource
from geoengine_openapi_client.models.layer_resource_id import LayerResourceId
from geoengine_openapi_client.models.layer_update import LayerUpdate
from geoengine_openapi_client.models.layer_visibility import LayerVisibility
from geoengine_openapi_client.models.line_symbology import LineSymbology
from geoengine_openapi_client.models.line_symbology_with_type import LineSymbologyWithType
from geoengine_openapi_client.models.linear_gradient import LinearGradient
from geoengine_openapi_client.models.linear_gradient_with_type import LinearGradientWithType
from geoengine_openapi_client.models.logarithmic_gradient import LogarithmicGradient
from geoengine_openapi_client.models.logarithmic_gradient_with_type import LogarithmicGradientWithType
from geoengine_openapi_client.models.measurement import Measurement
from geoengine_openapi_client.models.meta_data_definition import MetaDataDefinition
from geoengine_openapi_client.models.meta_data_suggestion import MetaDataSuggestion
from geoengine_openapi_client.models.mock_dataset_data_source_loading_info import MockDatasetDataSourceLoadingInfo
from geoengine_openapi_client.models.mock_meta_data import MockMetaData
from geoengine_openapi_client.models.mock_meta_data_with_type import MockMetaDataWithType
from geoengine_openapi_client.models.model_id_resource_id import ModelIdResourceId
from geoengine_openapi_client.models.multi_line_string import MultiLineString
from geoengine_openapi_client.models.multi_point import MultiPoint
from geoengine_openapi_client.models.multi_polygon import MultiPolygon
from geoengine_openapi_client.models.none_ogr_source_dataset_time_type import NoneOgrSourceDatasetTimeType
from geoengine_openapi_client.models.number_param import NumberParam
from geoengine_openapi_client.models.ogr_meta_data import OgrMetaData
from geoengine_openapi_client.models.ogr_meta_data_with_type import OgrMetaDataWithType
from geoengine_openapi_client.models.ogr_source_column_spec import OgrSourceColumnSpec
from geoengine_openapi_client.models.ogr_source_dataset import OgrSourceDataset
from geoengine_openapi_client.models.ogr_source_dataset_time_type import OgrSourceDatasetTimeType
from geoengine_openapi_client.models.ogr_source_duration_spec import OgrSourceDurationSpec
from geoengine_openapi_client.models.ogr_source_error_spec import OgrSourceErrorSpec
from geoengine_openapi_client.models.ogr_source_time_format import OgrSourceTimeFormat
from geoengine_openapi_client.models.order_by import OrderBy
from geoengine_openapi_client.models.over_under_colors import OverUnderColors
from geoengine_openapi_client.models.palette_colorizer import PaletteColorizer
from geoengine_openapi_client.models.permission import Permission
from geoengine_openapi_client.models.permission_request import PermissionRequest
from geoengine_openapi_client.models.plot import Plot
from geoengine_openapi_client.models.plot_output_format import PlotOutputFormat
from geoengine_openapi_client.models.plot_query_rectangle import PlotQueryRectangle
from geoengine_openapi_client.models.plot_result_descriptor import PlotResultDescriptor
from geoengine_openapi_client.models.plot_result_descriptor_with_type import PlotResultDescriptorWithType
from geoengine_openapi_client.models.plot_update import PlotUpdate
from geoengine_openapi_client.models.point_symbology import PointSymbology
from geoengine_openapi_client.models.point_symbology_with_type import PointSymbologyWithType
from geoengine_openapi_client.models.polygon_symbology import PolygonSymbology
from geoengine_openapi_client.models.polygon_symbology_with_type import PolygonSymbologyWithType
from geoengine_openapi_client.models.project import Project
from geoengine_openapi_client.models.project_layer import ProjectLayer
from geoengine_openapi_client.models.project_listing import ProjectListing
from geoengine_openapi_client.models.project_resource import ProjectResource
from geoengine_openapi_client.models.project_resource_id import ProjectResourceId
from geoengine_openapi_client.models.project_version import ProjectVersion
from geoengine_openapi_client.models.provenance import Provenance
from geoengine_openapi_client.models.provenance_entry import ProvenanceEntry
from geoengine_openapi_client.models.provenance_output import ProvenanceOutput
from geoengine_openapi_client.models.provider_layer_collection_id import ProviderLayerCollectionId
from geoengine_openapi_client.models.provider_layer_id import ProviderLayerId
from geoengine_openapi_client.models.quota import Quota
from geoengine_openapi_client.models.raster_data_type import RasterDataType
from geoengine_openapi_client.models.raster_dataset_from_workflow import RasterDatasetFromWorkflow
from geoengine_openapi_client.models.raster_dataset_from_workflow_result import RasterDatasetFromWorkflowResult
from geoengine_openapi_client.models.raster_properties_entry_type import RasterPropertiesEntryType
from geoengine_openapi_client.models.raster_properties_key import RasterPropertiesKey
from geoengine_openapi_client.models.raster_query_rectangle import RasterQueryRectangle
from geoengine_openapi_client.models.raster_result_descriptor import RasterResultDescriptor
from geoengine_openapi_client.models.raster_result_descriptor_with_type import RasterResultDescriptorWithType
from geoengine_openapi_client.models.raster_stream_websocket_result_type import RasterStreamWebsocketResultType
from geoengine_openapi_client.models.raster_symbology import RasterSymbology
from geoengine_openapi_client.models.raster_symbology_with_type import RasterSymbologyWithType
from geoengine_openapi_client.models.resource import Resource
from geoengine_openapi_client.models.resource_id import ResourceId
from geoengine_openapi_client.models.rgba_colorizer import RgbaColorizer
from geoengine_openapi_client.models.role import Role
from geoengine_openapi_client.models.role_description import RoleDescription
from geoengine_openapi_client.models.running_task_status import RunningTaskStatus
from geoengine_openapi_client.models.st_rectangle import STRectangle
from geoengine_openapi_client.models.server_info import ServerInfo
from geoengine_openapi_client.models.spatial_partition2_d import SpatialPartition2D
from geoengine_openapi_client.models.spatial_reference_authority import SpatialReferenceAuthority
from geoengine_openapi_client.models.spatial_reference_specification import SpatialReferenceSpecification
from geoengine_openapi_client.models.spatial_resolution import SpatialResolution
from geoengine_openapi_client.models.start_duration_ogr_source_dataset_time_type import StartDurationOgrSourceDatasetTimeType
from geoengine_openapi_client.models.start_end_ogr_source_dataset_time_type import StartEndOgrSourceDatasetTimeType
from geoengine_openapi_client.models.start_ogr_source_dataset_time_type import StartOgrSourceDatasetTimeType
from geoengine_openapi_client.models.static_color_param import StaticColorParam
from geoengine_openapi_client.models.static_number_param import StaticNumberParam
from geoengine_openapi_client.models.stroke_param import StrokeParam
from geoengine_openapi_client.models.symbology import Symbology
from geoengine_openapi_client.models.task_abort_options import TaskAbortOptions
from geoengine_openapi_client.models.task_filter import TaskFilter
from geoengine_openapi_client.models.task_list_options import TaskListOptions
from geoengine_openapi_client.models.task_response import TaskResponse
from geoengine_openapi_client.models.task_status import TaskStatus
from geoengine_openapi_client.models.task_status_with_id import TaskStatusWithId
from geoengine_openapi_client.models.text_symbology import TextSymbology
from geoengine_openapi_client.models.time_granularity import TimeGranularity
from geoengine_openapi_client.models.time_interval import TimeInterval
from geoengine_openapi_client.models.time_reference import TimeReference
from geoengine_openapi_client.models.time_step import TimeStep
from geoengine_openapi_client.models.time_step_with_type import TimeStepWithType
from geoengine_openapi_client.models.typed_geometry import TypedGeometry
from geoengine_openapi_client.models.typed_geometry_one_of import TypedGeometryOneOf
from geoengine_openapi_client.models.typed_geometry_one_of1 import TypedGeometryOneOf1
from geoengine_openapi_client.models.typed_geometry_one_of2 import TypedGeometryOneOf2
from geoengine_openapi_client.models.typed_geometry_one_of3 import TypedGeometryOneOf3
from geoengine_openapi_client.models.typed_operator import TypedOperator
from geoengine_openapi_client.models.typed_operator_operator import TypedOperatorOperator
from geoengine_openapi_client.models.typed_result_descriptor import TypedResultDescriptor
from geoengine_openapi_client.models.unitless_measurement import UnitlessMeasurement
from geoengine_openapi_client.models.unix_time_stamp_ogr_source_time_format import UnixTimeStampOgrSourceTimeFormat
from geoengine_openapi_client.models.unix_time_stamp_type import UnixTimeStampType
from geoengine_openapi_client.models.update_project import UpdateProject
from geoengine_openapi_client.models.update_quota import UpdateQuota
from geoengine_openapi_client.models.upload_file_layers_response import UploadFileLayersResponse
from geoengine_openapi_client.models.upload_files_response import UploadFilesResponse
from geoengine_openapi_client.models.user_credentials import UserCredentials
from geoengine_openapi_client.models.user_info import UserInfo
from geoengine_openapi_client.models.user_registration import UserRegistration
from geoengine_openapi_client.models.user_session import UserSession
from geoengine_openapi_client.models.vector_column_info import VectorColumnInfo
from geoengine_openapi_client.models.vector_data_type import VectorDataType
from geoengine_openapi_client.models.vector_query_rectangle import VectorQueryRectangle
from geoengine_openapi_client.models.vector_result_descriptor import VectorResultDescriptor
from geoengine_openapi_client.models.vector_result_descriptor_with_type import VectorResultDescriptorWithType
from geoengine_openapi_client.models.volume import Volume
from geoengine_openapi_client.models.wcs_boundingbox import WcsBoundingbox
from geoengine_openapi_client.models.wcs_service import WcsService
from geoengine_openapi_client.models.wcs_version import WcsVersion
from geoengine_openapi_client.models.wfs_service import WfsService
from geoengine_openapi_client.models.wfs_version import WfsVersion
from geoengine_openapi_client.models.wms_service import WmsService
from geoengine_openapi_client.models.wms_version import WmsVersion
from geoengine_openapi_client.models.workflow import Workflow
from geoengine_openapi_client.models.wrapped_plot_output import WrappedPlotOutput
from geoengine_openapi_client.models.zero_ogr_source_duration_spec import ZeroOgrSourceDurationSpec