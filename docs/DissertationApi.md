# osis_dissertation_sdk.DissertationApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/dissertation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dissertation_addjurymember**](DissertationApi.md#dissertation_addjurymember) | **POST** /dissertations/{uuid}/jury | 
[**dissertation_back_to_draft**](DissertationApi.md#dissertation_back_to_draft) | **POST** /dissertations/{uuid}/back_to_draft | 
[**dissertation_can_edit_dissertation**](DissertationApi.md#dissertation_can_edit_dissertation) | **GET** /dissertations/{uuid}/can_edit_dissertation | 
[**dissertation_can_manage_jury_member**](DissertationApi.md#dissertation_can_manage_jury_member) | **GET** /dissertations/{uuid}/can_manage_jury_member | 
[**dissertation_create**](DissertationApi.md#dissertation_create) | **POST** /dissertations | 
[**dissertation_deactivate**](DissertationApi.md#dissertation_deactivate) | **DELETE** /dissertations/{uuid}/ | 
[**dissertation_deletejurymember**](DissertationApi.md#dissertation_deletejurymember) | **DELETE** /dissertations/{uuid}/jury/{uuid_jury_member}/ | 
[**dissertation_detail**](DissertationApi.md#dissertation_detail) | **GET** /dissertations/{uuid}/ | 
[**dissertation_history**](DissertationApi.md#dissertation_history) | **GET** /dissertations/{uuid}/history | 
[**dissertation_list**](DissertationApi.md#dissertation_list) | **GET** /dissertations | 
[**dissertation_submit**](DissertationApi.md#dissertation_submit) | **POST** /dissertations/{uuid}/submit | 
[**dissertation_update**](DissertationApi.md#dissertation_update) | **PUT** /dissertations/{uuid}/ | 
[**retrieve_dissertation_file**](DissertationApi.md#retrieve_dissertation_file) | **GET** /dissertations/{uuid}/file | 
[**update_dissertation_file**](DissertationApi.md#update_dissertation_file) | **PUT** /dissertations/{uuid}/file | 


# **dissertation_addjurymember**
> DissertationJuryAddedResponse dissertation_addjurymember(uuid, dissertation_jury_add_command)



Add a reader jury member on dissertation

### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.dissertation_jury_added_response import DissertationJuryAddedResponse
from osis_dissertation_sdk.model.error import Error
from osis_dissertation_sdk.model.dissertation_jury_add_command import DissertationJuryAddCommand
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    uuid = "uuid_example" # str | 
    dissertation_jury_add_command = DissertationJuryAddCommand(
        adviser_uuid="f8b61488-f32b-4382-8633-3bf81fc5d6a5",
    ) # DissertationJuryAddCommand | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.dissertation_addjurymember(uuid, dissertation_jury_add_command)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_addjurymember: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.dissertation_addjurymember(uuid, dissertation_jury_add_command, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_addjurymember: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **dissertation_jury_add_command** | [**DissertationJuryAddCommand**](DissertationJuryAddCommand.md)|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**DissertationJuryAddedResponse**](DissertationJuryAddedResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissertation_back_to_draft**
> dissertation_back_to_draft(uuid, dissertation_back_to_draft_command)



Back to draft dissertation

### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.error import Error
from osis_dissertation_sdk.model.dissertation_back_to_draft_command import DissertationBackToDraftCommand
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    uuid = "uuid_example" # str | 
    dissertation_back_to_draft_command = DissertationBackToDraftCommand(
        justification="Raison du retour en brouillon",
    ) # DissertationBackToDraftCommand | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.dissertation_back_to_draft(uuid, dissertation_back_to_draft_command)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_back_to_draft: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.dissertation_back_to_draft(uuid, dissertation_back_to_draft_command, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_back_to_draft: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **dissertation_back_to_draft_command** | [**DissertationBackToDraftCommand**](DissertationBackToDraftCommand.md)|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was updated successfully. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissertation_can_edit_dissertation**
> DissertationCanEditDissertation dissertation_can_edit_dissertation(uuid)



Can edit dissertation

### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.dissertation_can_edit_dissertation import DissertationCanEditDissertation
from osis_dissertation_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.dissertation_can_edit_dissertation(uuid)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_can_edit_dissertation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.dissertation_can_edit_dissertation(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_can_edit_dissertation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**DissertationCanEditDissertation**](DissertationCanEditDissertation.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissertation_can_manage_jury_member**
> DissertationCanManageJury dissertation_can_manage_jury_member(uuid)



Can manage jury on this dissertation

### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.dissertation_can_manage_jury import DissertationCanManageJury
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.dissertation_can_manage_jury_member(uuid)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_can_manage_jury_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.dissertation_can_manage_jury_member(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_can_manage_jury_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**DissertationCanManageJury**](DissertationCanManageJury.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissertation_create**
> DissertationCreatedResponse dissertation_create(dissertation_create_command)



Create a dissertation

### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.dissertation_created_response import DissertationCreatedResponse
from osis_dissertation_sdk.model.dissertation_create_command import DissertationCreateCommand
from osis_dissertation_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    dissertation_create_command = DissertationCreateCommand(
        proposition_dissertation_uuid="f8b61488-f32b-4382-8633-3bf81fc5d6a5",
        title="Big data, l'or numérique",
        description="Mémoire portant sur le big data",
        defend_year=2019,
        defend_period=DefendPeriodEnum("UNDEFINED"),
        location_uuid="f8b61488-f32b-4382-8633-3bf81fc5d6a5",
        acronym="PSY2MS/PS",
        year=2020,
    ) # DissertationCreateCommand | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.dissertation_create(dissertation_create_command)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.dissertation_create(dissertation_create_command, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dissertation_create_command** | [**DissertationCreateCommand**](DissertationCreateCommand.md)|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**DissertationCreatedResponse**](DissertationCreatedResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissertation_deactivate**
> dissertation_deactivate(uuid)



Deactivate a dissertation of the current user

### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.dissertation_deactivate(uuid)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_deactivate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.dissertation_deactivate(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_deactivate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissertation_deletejurymember**
> dissertation_deletejurymember(uuid, uuid_jury_member)



Delete a jury member of dissertation

### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    uuid = "uuid_example" # str | 
    uuid_jury_member = "uuid_jury_member_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.dissertation_deletejurymember(uuid, uuid_jury_member)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_deletejurymember: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.dissertation_deletejurymember(uuid, uuid_jury_member, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_deletejurymember: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **uuid_jury_member** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissertation_detail**
> DissertationDetail dissertation_detail(uuid)



Return dissertation's detail of the user currently connected

### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.error import Error
from osis_dissertation_sdk.model.dissertation_detail import DissertationDetail
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.dissertation_detail(uuid)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.dissertation_detail(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**DissertationDetail**](DissertationDetail.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissertation_history**
> DissertationHistoryPaginatedList dissertation_history(uuid)



Return dissertation's modification history

### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.dissertation_history_paginated_list import DissertationHistoryPaginatedList
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.dissertation_history(uuid)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.dissertation_history(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**DissertationHistoryPaginatedList**](DissertationHistoryPaginatedList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissertation_list**
> DissertationPaginatedList dissertation_list()



Return all dissertations of connected user

### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.dissertation_paginated_list import DissertationPaginatedList
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    search = "search_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.dissertation_list(limit=limit, offset=offset, search=search, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **search** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**DissertationPaginatedList**](DissertationPaginatedList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissertation_submit**
> dissertation_submit(uuid, dissertation_submit_command)



Submit dissertation

### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.error import Error
from osis_dissertation_sdk.model.dissertation_submit_command import DissertationSubmitCommand
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    uuid = "uuid_example" # str | 
    dissertation_submit_command = DissertationSubmitCommand(
        justification="Raison de la soumission",
    ) # DissertationSubmitCommand | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.dissertation_submit(uuid, dissertation_submit_command)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_submit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.dissertation_submit(uuid, dissertation_submit_command, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_submit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **dissertation_submit_command** | [**DissertationSubmitCommand**](DissertationSubmitCommand.md)|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was updated successfully. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissertation_update**
> dissertation_update(uuid, dissertation_update_command)



Update user's dissertation

### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.dissertation_update_command import DissertationUpdateCommand
from osis_dissertation_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    uuid = "uuid_example" # str | 
    dissertation_update_command = DissertationUpdateCommand(
        title="Big data, l'or numérique",
        description="Mémoire portant sur le big data",
        defend_year=2019,
        defend_period=DefendPeriodEnum("UNDEFINED"),
        location_uuid="f8b61488-f32b-4382-8633-3bf81fc5d6a5",
    ) # DissertationUpdateCommand | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.dissertation_update(uuid, dissertation_update_command)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.dissertation_update(uuid, dissertation_update_command, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->dissertation_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **dissertation_update_command** | [**DissertationUpdateCommand**](DissertationUpdateCommand.md)|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was been updated successfully. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_dissertation_file**
> DissertationFile retrieve_dissertation_file(uuid)



### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.dissertation_file import DissertationFile
from osis_dissertation_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    uuid = "uuid_example" # str | The uuid of the dissertation
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_dissertation_file(uuid)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->retrieve_dissertation_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_dissertation_file(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->retrieve_dissertation_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the dissertation |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**DissertationFile**](DissertationFile.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dissertation_file**
> DissertationFile update_dissertation_file(uuid)



### Example

* Api Key Authentication (Token):

```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import dissertation_api
from osis_dissertation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_dissertation_sdk.model.dissertation_file import DissertationFile
from osis_dissertation_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/dissertation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_dissertation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/dissertation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_dissertation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dissertation_api.DissertationApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    dissertation_file = DissertationFile(
        dissertation_file=[
            "dissertation_file_example",
        ],
    ) # DissertationFile |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_dissertation_file(uuid)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->update_dissertation_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_dissertation_file(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, dissertation_file=dissertation_file)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling DissertationApi->update_dissertation_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **dissertation_file** | [**DissertationFile**](DissertationFile.md)|  | [optional]

### Return type

[**DissertationFile**](DissertationFile.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

