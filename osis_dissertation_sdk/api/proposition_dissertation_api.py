"""
    Dissertation Service

    A set of API endpoints that allow you to get information about dissertation  # noqa: E501

    The version of the OpenAPI document: 1.00
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from osis_dissertation_sdk.api_client import ApiClient, Endpoint as _Endpoint
from osis_dissertation_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.error import Error
from osis_dissertation_sdk.model.proposition_dissertation_detail import PropositionDissertationDetail
from osis_dissertation_sdk.model.proposition_dissertation_file import PropositionDissertationFile
from osis_dissertation_sdk.model.proposition_dissertation_paginated_list import PropositionDissertationPaginatedList


class PropositionDissertationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.proposition_detail_endpoint = _Endpoint(
            settings={
                'response_type': (PropositionDissertationDetail,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/propositions/{uuid}/',
                'operation_id': 'proposition_detail',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'uuid',
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                ],
                'required': [
                    'uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'uuid':
                        (str,),
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                },
                'attribute_map': {
                    'uuid': 'uuid',
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                },
                'location_map': {
                    'uuid': 'path',
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.propositions_list_endpoint = _Endpoint(
            settings={
                'response_type': (PropositionDissertationPaginatedList,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/propositions',
                'operation_id': 'propositions_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'offset',
                    'search',
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'search':
                        (str,),
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'offset': 'offset',
                    'search': 'search',
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                },
                'location_map': {
                    'limit': 'query',
                    'offset': 'query',
                    'search': 'query',
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.retrieve_proposition_dissertation_file_endpoint = _Endpoint(
            settings={
                'response_type': (PropositionDissertationFile,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/propositions/{uuid}/file',
                'operation_id': 'retrieve_proposition_dissertation_file',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'uuid',
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                ],
                'required': [
                    'uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'uuid':
                        (str,),
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                },
                'attribute_map': {
                    'uuid': 'uuid',
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                },
                'location_map': {
                    'uuid': 'path',
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_proposition_dissertation_file_endpoint = _Endpoint(
            settings={
                'response_type': (PropositionDissertationFile,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/propositions/{uuid}/file',
                'operation_id': 'update_proposition_dissertation_file',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'uuid',
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                    'proposition_dissertation_file',
                ],
                'required': [
                    'uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'uuid':
                        (str,),
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                    'proposition_dissertation_file':
                        (PropositionDissertationFile,),
                },
                'attribute_map': {
                    'uuid': 'uuid',
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                },
                'location_map': {
                    'uuid': 'path',
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                    'proposition_dissertation_file': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def proposition_detail(
        self,
        uuid,
        **kwargs
    ):
        """proposition_detail  # noqa: E501

        Return detail of a proposition dissertation available for the user currently connected  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.proposition_detail(uuid, async_req=True)
        >>> result = thread.get()

        Args:
            uuid (str):

        Keyword Args:
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) . [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PropositionDissertationDetail
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['uuid'] = \
            uuid
        return self.proposition_detail_endpoint.call_with_http_info(**kwargs)

    def propositions_list(
        self,
        **kwargs
    ):
        """propositions_list  # noqa: E501

        Return all dissertation's propositions available for the user currently connected  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.propositions_list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit (int): [optional]
            offset (int): [optional]
            search (str): [optional]
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) . [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PropositionDissertationPaginatedList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.propositions_list_endpoint.call_with_http_info(**kwargs)

    def retrieve_proposition_dissertation_file(
        self,
        uuid,
        **kwargs
    ):
        """retrieve_proposition_dissertation_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.retrieve_proposition_dissertation_file(uuid, async_req=True)
        >>> result = thread.get()

        Args:
            uuid (str): The uuid of the proposition dissertation

        Keyword Args:
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) . [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PropositionDissertationFile
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['uuid'] = \
            uuid
        return self.retrieve_proposition_dissertation_file_endpoint.call_with_http_info(**kwargs)

    def update_proposition_dissertation_file(
        self,
        uuid,
        **kwargs
    ):
        """update_proposition_dissertation_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_proposition_dissertation_file(uuid, async_req=True)
        >>> result = thread.get()

        Args:
            uuid (str):

        Keyword Args:
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) . [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
            proposition_dissertation_file (PropositionDissertationFile): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PropositionDissertationFile
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['uuid'] = \
            uuid
        return self.update_proposition_dissertation_file_endpoint.call_with_http_info(**kwargs)

