"""
    DM.API Account

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401
import allure

from dm_api_account.api_client import ApiClient, Endpoint as _Endpoint
from dm_api_account.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from dm_api_account.model.bad_request_error import BadRequestError
from dm_api_account.model.change_email import ChangeEmail
from dm_api_account.model.change_password import ChangePassword
from dm_api_account.model.general_error import GeneralError
from dm_api_account.model.registration import Registration
from dm_api_account.model.reset_password import ResetPassword
from dm_api_account.model.user_details_envelope import UserDetailsEnvelope
from dm_api_account.model.user_envelope import UserEnvelope


class AccountApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
	
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        @allure.step("Activate registered user")
        def __activate(
            self,
            token,
            **kwargs
        ):
            """Activate registered user  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.activate(token, async_req=True)
            >>> result = thread.get()

            Args:
                token (str): Activation token

            Keyword Args:
                x_dm_auth_token (str): Authenticated requests require X-Dm-Auth-Token header. You can get the data from POST /account/ method, sending login and password in \"token\" response field. [optional]
                x_dm_bb_render_mode (str): Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UserEnvelope
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['token'] = \
                token
            return self.call_with_http_info(**kwargs)

        self.activate = _Endpoint(
            settings={
                'response_type': (UserEnvelope,),
                'auth': [],
                'endpoint_path': '/v1/account/{token}',
                'operation_id': 'activate',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'token',
                    'x_dm_auth_token',
                    'x_dm_bb_render_mode',
                ],
                'required': [
                    'token',
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
                    'token':
                        (str,),
                    'x_dm_auth_token':
                        (str,),
                    'x_dm_bb_render_mode':
                        (str,),
                },
                'attribute_map': {
                    'token': 'token',
                    'x_dm_auth_token': 'X-Dm-Auth-Token',
                    'x_dm_bb_render_mode': 'X-Dm-Bb-Render-Mode',
                },
                'location_map': {
                    'token': 'path',
                    'x_dm_auth_token': 'header',
                    'x_dm_bb_render_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__activate
        )

        @allure.step("Change registered user email")
        def __change_email(
            self,
            **kwargs
        ):
            """Change registered user email  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.change_email(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                x_dm_auth_token (str): Authenticated requests require X-Dm-Auth-Token header. You can get the data from POST /account/ method, sending login and password in \"token\" response field. [optional]
                x_dm_bb_render_mode (str): Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml. [optional]
                change_email (ChangeEmail): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UserEnvelope
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.change_email = _Endpoint(
            settings={
                'response_type': (UserEnvelope,),
                'auth': [],
                'endpoint_path': '/v1/account/email',
                'operation_id': 'change_email',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_dm_auth_token',
                    'x_dm_bb_render_mode',
                    'change_email',
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
                    'x_dm_auth_token':
                        (str,),
                    'x_dm_bb_render_mode':
                        (str,),
                    'change_email':
                        (ChangeEmail,),
                },
                'attribute_map': {
                    'x_dm_auth_token': 'X-Dm-Auth-Token',
                    'x_dm_bb_render_mode': 'X-Dm-Bb-Render-Mode',
                },
                'location_map': {
                    'x_dm_auth_token': 'header',
                    'x_dm_bb_render_mode': 'header',
                    'change_email': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__change_email
        )

        @allure.step("Change registered user password")
        def __change_password(
            self,
            **kwargs
        ):
            """Change registered user password  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.change_password(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                x_dm_auth_token (str): Authenticated requests require X-Dm-Auth-Token header. You can get the data from POST /account/ method, sending login and password in \"token\" response field. [optional]
                x_dm_bb_render_mode (str): Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml. [optional]
                change_password (ChangePassword): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UserEnvelope
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.change_password = _Endpoint(
            settings={
                'response_type': (UserEnvelope,),
                'auth': [],
                'endpoint_path': '/v1/account/password',
                'operation_id': 'change_password',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_dm_auth_token',
                    'x_dm_bb_render_mode',
                    'change_password',
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
                    'x_dm_auth_token':
                        (str,),
                    'x_dm_bb_render_mode':
                        (str,),
                    'change_password':
                        (ChangePassword,),
                },
                'attribute_map': {
                    'x_dm_auth_token': 'X-Dm-Auth-Token',
                    'x_dm_bb_render_mode': 'X-Dm-Bb-Render-Mode',
                },
                'location_map': {
                    'x_dm_auth_token': 'header',
                    'x_dm_bb_render_mode': 'header',
                    'change_password': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__change_password
        )

        @allure.step("Get current user")
        def __get_current(
            self,
            x_dm_auth_token,
            **kwargs
        ):
            """Get current user  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_current(x_dm_auth_token, async_req=True)
            >>> result = thread.get()

            Args:
                x_dm_auth_token (str): Authenticated requests require X-Dm-Auth-Token header. You can get the data from POST /account/ method, sending login and password in \"token\" response field

            Keyword Args:
                x_dm_bb_render_mode (str): Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UserDetailsEnvelope
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_dm_auth_token'] = \
                x_dm_auth_token
            return self.call_with_http_info(**kwargs)

        self.get_current = _Endpoint(
            settings={
                'response_type': (UserDetailsEnvelope,),
                'auth': [],
                'endpoint_path': '/v1/account',
                'operation_id': 'get_current',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_dm_auth_token',
                    'x_dm_bb_render_mode',
                ],
                'required': [
                    'x_dm_auth_token',
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
                    'x_dm_auth_token':
                        (str,),
                    'x_dm_bb_render_mode':
                        (str,),
                },
                'attribute_map': {
                    'x_dm_auth_token': 'X-Dm-Auth-Token',
                    'x_dm_bb_render_mode': 'X-Dm-Bb-Render-Mode',
                },
                'location_map': {
                    'x_dm_auth_token': 'header',
                    'x_dm_bb_render_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_current
        )

        @allure.step("Register new user")
        def __register(
            self,
            **kwargs
        ):
            """Register new user  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.register(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                x_dm_auth_token (str): Authenticated requests require X-Dm-Auth-Token header. You can get the data from POST /account/ method, sending login and password in \"token\" response field. [optional]
                x_dm_bb_render_mode (str): Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml. [optional]
                registration (Registration): New user credentials information. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.register = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/v1/account',
                'operation_id': 'register',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_dm_auth_token',
                    'x_dm_bb_render_mode',
                    'registration',
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
                    'x_dm_auth_token':
                        (str,),
                    'x_dm_bb_render_mode':
                        (str,),
                    'registration':
                        (Registration,),
                },
                'attribute_map': {
                    'x_dm_auth_token': 'X-Dm-Auth-Token',
                    'x_dm_bb_render_mode': 'X-Dm-Bb-Render-Mode',
                },
                'location_map': {
                    'x_dm_auth_token': 'header',
                    'x_dm_bb_render_mode': 'header',
                    'registration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__register
        )

        @allure.step("Reset registered user password")
        def __reset_password(
            self,
            **kwargs
        ):
            """Reset registered user password  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.reset_password(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                x_dm_auth_token (str): Authenticated requests require X-Dm-Auth-Token header. You can get the data from POST /account/ method, sending login and password in \"token\" response field. [optional]
                x_dm_bb_render_mode (str): Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml. [optional]
                reset_password (ResetPassword): Account details. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.reset_password = _Endpoint(
            settings={
                'response_type': (UserEnvelope,),
                'auth': [],
                'endpoint_path': '/v1/account/password',
                'operation_id': 'reset_password',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_dm_auth_token',
                    'x_dm_bb_render_mode',
                    'reset_password',
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
                    'x_dm_auth_token':
                        (str,),
                    'x_dm_bb_render_mode':
                        (str,),
                    'reset_password':
                        (ResetPassword,),
                },
                'attribute_map': {
                    'x_dm_auth_token': 'X-Dm-Auth-Token',
                    'x_dm_bb_render_mode': 'X-Dm-Bb-Render-Mode',
                },
                'location_map': {
                    'x_dm_auth_token': 'header',
                    'x_dm_bb_render_mode': 'header',
                    'reset_password': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__reset_password
        )
