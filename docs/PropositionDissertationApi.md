# osis_dissertation_sdk.PropositionDissertationApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/dissertation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proposition_detail**](PropositionDissertationApi.md#proposition_detail) | **GET** /propositions/{uuid}/ | 
[**propositions_list**](PropositionDissertationApi.md#propositions_list) | **GET** /propositions | 


# **proposition_detail**
> PropositionDissertationDetail proposition_detail(uuid)



Return detail of a proposition dissertation available for the user currently connected

### Example

* Api Key Authentication (Token):
```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import proposition_dissertation_api
from osis_dissertation_sdk.model.proposition_dissertation_detail import PropositionDissertationDetail
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
    api_instance = proposition_dissertation_api.PropositionDissertationApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.proposition_detail(uuid)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling PropositionDissertationApi->proposition_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.proposition_detail(uuid, accept_language=accept_language)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling PropositionDissertationApi->proposition_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]

### Return type

[**PropositionDissertationDetail**](PropositionDissertationDetail.md)

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

# **propositions_list**
> object propositions_list()



Return all dissertation's propositions available for the user currently connected

### Example

* Api Key Authentication (Token):
```python
import time
import osis_dissertation_sdk
from osis_dissertation_sdk.api import proposition_dissertation_api
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
    api_instance = proposition_dissertation_api.PropositionDissertationApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    search = "search_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.propositions_list(limit=limit, offset=offset, search=search, accept_language=accept_language)
        pprint(api_response)
    except osis_dissertation_sdk.ApiException as e:
        print("Exception when calling PropositionDissertationApi->propositions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **search** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]

### Return type

**object**

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

