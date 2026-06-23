# currencycore.CurrencyCoreApi

All URIs are relative to *https://api.currency-core.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai**](CurrencyCoreApi.md#ai) | **GET** /ai | AI
[**convert**](CurrencyCoreApi.md#convert) | **GET** /convert | Convert
[**correlation**](CurrencyCoreApi.md#correlation) | **GET** /correlation | Correlation
[**countries**](CurrencyCoreApi.md#countries) | **GET** /countries | Countries
[**currencies**](CurrencyCoreApi.md#currencies) | **GET** /currencies | Currencies
[**drawdown**](CurrencyCoreApi.md#drawdown) | **GET** /drawdown | Drawdown
[**history**](CurrencyCoreApi.md#history) | **GET** /history | History
[**history_analysis**](CurrencyCoreApi.md#history_analysis) | **GET** /history/analysis | History analysis
[**mean_reversion**](CurrencyCoreApi.md#mean_reversion) | **GET** /mean-reversion | Mean reversion
[**ppp_analysis**](CurrencyCoreApi.md#ppp_analysis) | **GET** /ppp/analysis | PPP analysis
[**rates**](CurrencyCoreApi.md#rates) | **GET** /rates | Rates
[**rates_by_base**](CurrencyCoreApi.md#rates_by_base) | **GET** /rates/{base} | Rates by base
[**safe_haven**](CurrencyCoreApi.md#safe_haven) | **GET** /safe-haven | Safe haven
[**volatility**](CurrencyCoreApi.md#volatility) | **GET** /volatility | Volatility


# **ai**
> AiResponse ai(q)

AI

Ask a natural-language currency question; the model answers using live rates.

### Example

* Bearer Authentication (bearerAuth):

```python
import currencycore
from currencycore.models.ai_response import AiResponse
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = currencycore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)
    q = 'Convert 50 euro to indian rupees' # str | A natural-language question, e.g. \"Convert 50 euro to indian rupees\" or \"What's the USD to EUR rate today?\".

    try:
        # AI
        api_response = api_instance.ai(q)
        print("The response of CurrencyCoreApi->ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->ai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| A natural-language question, e.g. \&quot;Convert 50 euro to indian rupees\&quot; or \&quot;What&#39;s the USD to EUR rate today?\&quot;. | 

### Return type

[**AiResponse**](AiResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**429** | Rate limit or monthly quota exceeded. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert**
> ConvertResponse convert(var_from, to, amount=amount, ppp=ppp, var_date=var_date)

Convert

Convert an amount between currencies, optionally PPP-adjusted.

### Example

* Bearer Authentication (bearerAuth):

```python
import currencycore
from currencycore.models.convert_response import ConvertResponse
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = currencycore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)
    var_from = 'USD' # str | Source currency (ISO 4217), e.g. USD. For PPP (ppp=true) pair it with a country as CUR:COUNTRY, e.g. USD:USA.
    to = 'EUR,INR' # str | One or more target currencies, comma-separated, e.g. EUR,INR (max 25). For PPP use CUR:COUNTRY pairs, e.g. EUR:DEU,INR:IND.
    amount = 100 # float | Amount to convert. Optional, defaults to 1 (so each result equals the rate). (optional)
    ppp = false # bool | When true, apply a PPP adjustment. Every currency must then carry a country code. (optional)
    var_date = 'var_date_example' # str | Rate date in YYYY-MM-DD (UTC). Must not be in the future. Defaults to latest. (optional)

    try:
        # Convert
        api_response = api_instance.convert(var_from, to, amount=amount, ppp=ppp, var_date=var_date)
        print("The response of CurrencyCoreApi->convert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->convert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| Source currency (ISO 4217), e.g. USD. For PPP (ppp&#x3D;true) pair it with a country as CUR:COUNTRY, e.g. USD:USA. | 
 **to** | **str**| One or more target currencies, comma-separated, e.g. EUR,INR (max 25). For PPP use CUR:COUNTRY pairs, e.g. EUR:DEU,INR:IND. | 
 **amount** | **float**| Amount to convert. Optional, defaults to 1 (so each result equals the rate). | [optional] 
 **ppp** | **bool**| When true, apply a PPP adjustment. Every currency must then carry a country code. | [optional] 
 **var_date** | **str**| Rate date in YYYY-MM-DD (UTC). Must not be in the future. Defaults to latest. | [optional] 

### Return type

[**ConvertResponse**](ConvertResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**429** | Rate limit or monthly quota exceeded. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **correlation**
> CorrelationResponse correlation(currencies, base=base, var_from=var_from, to=to)

Correlation

Correlation of each currency's daily returns with a base currency's, over a window. Growth plan or higher.

### Example

* Bearer Authentication (bearerAuth):

```python
import currencycore
from currencycore.models.correlation_response import CorrelationResponse
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = currencycore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)
    currencies = 'GBP,CHF,SEK' # str | Comma-separated currencies to correlate with `base`, e.g. GBP,CHF,SEK.
    base = 'EUR' # str | Reference currency to correlate against (3-letter ISO 4217). Defaults to USD (a non-USD base is more meaningful). (optional)
    var_from = 'var_from_example' # str | Window start YYYY-MM-DD (UTC). Defaults to 365 days before `to`. (optional)
    to = 'to_example' # str | Window end YYYY-MM-DD (UTC). Defaults to today. (optional)

    try:
        # Correlation
        api_response = api_instance.correlation(currencies, base=base, var_from=var_from, to=to)
        print("The response of CurrencyCoreApi->correlation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->correlation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencies** | **str**| Comma-separated currencies to correlate with &#x60;base&#x60;, e.g. GBP,CHF,SEK. | 
 **base** | **str**| Reference currency to correlate against (3-letter ISO 4217). Defaults to USD (a non-USD base is more meaningful). | [optional] 
 **var_from** | **str**| Window start YYYY-MM-DD (UTC). Defaults to 365 days before &#x60;to&#x60;. | [optional] 
 **to** | **str**| Window end YYYY-MM-DD (UTC). Defaults to today. | [optional] 

### Return type

[**CorrelationResponse**](CorrelationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Requires the growth plan or higher. |  -  |
**429** | Rate limit or monthly quota exceeded. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **countries**
> List[CountriesResponseInner] countries()

Countries

The supported countries and their official currencies. Public, no key needed.

### Example


```python
import currencycore
from currencycore.models.countries_response_inner import CountriesResponseInner
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)


# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)

    try:
        # Countries
        api_response = api_instance.countries()
        print("The response of CurrencyCoreApi->countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->countries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CountriesResponseInner]**](CountriesResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currencies**
> List[CurrenciesResponseInner] currencies()

Currencies

The full list of supported ISO 4217 currencies. Use it to resolve a name or symbol to its code, or to check whether a currency is supported (so a missing one fails clearly, not silently). Public, no key needed.

### Example


```python
import currencycore
from currencycore.models.currencies_response_inner import CurrenciesResponseInner
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)


# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)

    try:
        # Currencies
        api_response = api_instance.currencies()
        print("The response of CurrencyCoreApi->currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->currencies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CurrenciesResponseInner]**](CurrenciesResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drawdown**
> DrawdownResponse drawdown(currency=currency, base=base, var_from=var_from, to=to, sort=sort, universe=universe, limit=limit)

Drawdown

Maximum peak-to-trough decline vs a base (with peak/trough/recovery), or a drawdown ranking. Growth plan or higher.

### Example

* Bearer Authentication (bearerAuth):

```python
import currencycore
from currencycore.models.drawdown_response import DrawdownResponse
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = currencycore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)
    currency = 'EUR' # str | Currency to measure (3-letter ISO 4217), or a comma-separated list. OMIT to RANK the liquid set by drawdown. (optional)
    base = 'USD' # str | Base currency to measure against (3-letter ISO 4217). Defaults to USD. (optional)
    var_from = 'var_from_example' # str | Window start YYYY-MM-DD (UTC). Defaults to 365 days before `to`. (optional)
    to = 'to_example' # str | Window end YYYY-MM-DD (UTC). Defaults to today. (optional)
    sort = 'deepest' # str | Ranking direction: deepest (largest decline first, default) or recovery (fastest recovery first). (optional)
    universe = 'liquid' # str | Ranking universe: liquid (default) or majors. (optional)
    limit = 10 # float | Ranking: how many to return (default 10, max 50). (optional)

    try:
        # Drawdown
        api_response = api_instance.drawdown(currency=currency, base=base, var_from=var_from, to=to, sort=sort, universe=universe, limit=limit)
        print("The response of CurrencyCoreApi->drawdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->drawdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency to measure (3-letter ISO 4217), or a comma-separated list. OMIT to RANK the liquid set by drawdown. | [optional] 
 **base** | **str**| Base currency to measure against (3-letter ISO 4217). Defaults to USD. | [optional] 
 **var_from** | **str**| Window start YYYY-MM-DD (UTC). Defaults to 365 days before &#x60;to&#x60;. | [optional] 
 **to** | **str**| Window end YYYY-MM-DD (UTC). Defaults to today. | [optional] 
 **sort** | **str**| Ranking direction: deepest (largest decline first, default) or recovery (fastest recovery first). | [optional] 
 **universe** | **str**| Ranking universe: liquid (default) or majors. | [optional] 
 **limit** | **float**| Ranking: how many to return (default 10, max 50). | [optional] 

### Return type

[**DrawdownResponse**](DrawdownResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Requires the growth plan or higher. |  -  |
**429** | Rate limit or monthly quota exceeded. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history**
> HistoryResponse history(currency, var_from=var_from, to=to, base=base, interval=interval)

History

A single currency's daily rate time series over a date range. Growth plan or higher.

### Example

* Bearer Authentication (bearerAuth):

```python
import currencycore
from currencycore.models.history_response import HistoryResponse
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = currencycore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)
    currency = 'INR' # str | The currency whose history to fetch (3-letter ISO 4217), e.g. INR. One currency per call.
    var_from = 'var_from_example' # str | Start date YYYY-MM-DD (UTC). Defaults to 7 days before `to`. (optional)
    to = 'to_example' # str | End date YYYY-MM-DD (UTC). Defaults to today; a future date clamps to today. (optional)
    base = 'USD' # str | Base currency the rates are expressed against (3-letter ISO 4217). Defaults to USD. (optional)
    interval = 'daily' # str | Aggregation: daily (default), weekly, monthly, or yearly. Coarser intervals average the daily rates per bucket (weekly key = the week's Monday, monthly = YYYY-MM, yearly = YYYY). (optional)

    try:
        # History
        api_response = api_instance.history(currency, var_from=var_from, to=to, base=base, interval=interval)
        print("The response of CurrencyCoreApi->history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency whose history to fetch (3-letter ISO 4217), e.g. INR. One currency per call. | 
 **var_from** | **str**| Start date YYYY-MM-DD (UTC). Defaults to 7 days before &#x60;to&#x60;. | [optional] 
 **to** | **str**| End date YYYY-MM-DD (UTC). Defaults to today; a future date clamps to today. | [optional] 
 **base** | **str**| Base currency the rates are expressed against (3-letter ISO 4217). Defaults to USD. | [optional] 
 **interval** | **str**| Aggregation: daily (default), weekly, monthly, or yearly. Coarser intervals average the daily rates per bucket (weekly key &#x3D; the week&#39;s Monday, monthly &#x3D; YYYY-MM, yearly &#x3D; YYYY). | [optional] 

### Return type

[**HistoryResponse**](HistoryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Requires the growth plan or higher. |  -  |
**429** | Rate limit or monthly quota exceeded. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history_analysis**
> HistoryAnalysisResponse history_analysis(base=base, currencies=currencies, var_from=var_from, to=to, period=period, sort=sort, asset_class=asset_class, limit=limit, interval=interval, stats=stats)

History analysis

Trends, comparisons & 'movers': % change, strength, and min/max/avg over a window. Growth plan or higher.

### Example

* Bearer Authentication (bearerAuth):

```python
import currencycore
from currencycore.models.history_analysis_response import HistoryAnalysisResponse
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = currencycore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)
    base = 'USD' # str | Currency everything is measured against (3-letter ISO 4217). Defaults to USD. (optional)
    currencies = 'GBP,EUR,AED' # str | Comma-separated currencies to compare, e.g. GBP,EUR,AED. OMIT to rank ALL currencies vs base ('movers' mode). (optional)
    var_from = 'var_from_example' # str | Window start YYYY-MM-DD (UTC). Defaults to 20 years (2 decades) before `to`. See `period` for a shorthand. (optional)
    to = 'to_example' # str | Window end YYYY-MM-DD (UTC). Defaults to today; a future date clamps to today. (optional)
    period = '10y' # str | Relative window shorthand for `from`: e.g. 10y, 6m, 30d, ytd, max. Ignored if `from` is given. (optional)
    sort = 'strengthened' # str | Movers ranking: strengthened (default) or weakened. (optional)
    asset_class = 'fiat' # str | Movers universe: fiat (default, the liquid tradeable currencies), metals (XAU/XAG/XPT/XPD), or all (every currency incl. illiquid/frontier). fiat excludes metals/synthetics + illiquid frontier codes; redenomination artifacts are always dropped. (optional)
    limit = 10 # float | Movers: how many top results to return (default 10, max 200). (optional)
    interval = 'yearly' # str | Attach a trend series per named currency: weekly, monthly, or yearly (compare mode only). (optional)
    stats = true # bool | Include min/max/avg over the window per currency. Defaults to true; pass false to skip. (optional)

    try:
        # History analysis
        api_response = api_instance.history_analysis(base=base, currencies=currencies, var_from=var_from, to=to, period=period, sort=sort, asset_class=asset_class, limit=limit, interval=interval, stats=stats)
        print("The response of CurrencyCoreApi->history_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->history_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base** | **str**| Currency everything is measured against (3-letter ISO 4217). Defaults to USD. | [optional] 
 **currencies** | **str**| Comma-separated currencies to compare, e.g. GBP,EUR,AED. OMIT to rank ALL currencies vs base (&#39;movers&#39; mode). | [optional] 
 **var_from** | **str**| Window start YYYY-MM-DD (UTC). Defaults to 20 years (2 decades) before &#x60;to&#x60;. See &#x60;period&#x60; for a shorthand. | [optional] 
 **to** | **str**| Window end YYYY-MM-DD (UTC). Defaults to today; a future date clamps to today. | [optional] 
 **period** | **str**| Relative window shorthand for &#x60;from&#x60;: e.g. 10y, 6m, 30d, ytd, max. Ignored if &#x60;from&#x60; is given. | [optional] 
 **sort** | **str**| Movers ranking: strengthened (default) or weakened. | [optional] 
 **asset_class** | **str**| Movers universe: fiat (default, the liquid tradeable currencies), metals (XAU/XAG/XPT/XPD), or all (every currency incl. illiquid/frontier). fiat excludes metals/synthetics + illiquid frontier codes; redenomination artifacts are always dropped. | [optional] 
 **limit** | **float**| Movers: how many top results to return (default 10, max 200). | [optional] 
 **interval** | **str**| Attach a trend series per named currency: weekly, monthly, or yearly (compare mode only). | [optional] 
 **stats** | **bool**| Include min/max/avg over the window per currency. Defaults to true; pass false to skip. | [optional] 

### Return type

[**HistoryAnalysisResponse**](HistoryAnalysisResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Requires the growth plan or higher. |  -  |
**429** | Rate limit or monthly quota exceeded. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mean_reversion**
> MeanReversionResponse mean_reversion(currencies=currencies, base=base, var_from=var_from, to=to, limit=limit)

Mean reversion

Ranks currencies by how strongly they revert to their mean (crossing frequency + reversion half-life). Growth plan or higher.

### Example

* Bearer Authentication (bearerAuth):

```python
import currencycore
from currencycore.models.mean_reversion_response import MeanReversionResponse
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = currencycore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)
    currencies = 'EUR,GBP' # str | Comma-separated currencies to score, e.g. EUR,GBP. OMIT to rank the liquid set. (optional)
    base = 'USD' # str | Base currency to measure against (3-letter ISO 4217). Defaults to USD. (optional)
    var_from = 'var_from_example' # str | Window start YYYY-MM-DD (UTC). Defaults to ~2 years before `to`. (optional)
    to = 'to_example' # str | Window end YYYY-MM-DD (UTC). Defaults to today. (optional)
    limit = 10 # float | How many to return (default 10, max 50). (optional)

    try:
        # Mean reversion
        api_response = api_instance.mean_reversion(currencies=currencies, base=base, var_from=var_from, to=to, limit=limit)
        print("The response of CurrencyCoreApi->mean_reversion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->mean_reversion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencies** | **str**| Comma-separated currencies to score, e.g. EUR,GBP. OMIT to rank the liquid set. | [optional] 
 **base** | **str**| Base currency to measure against (3-letter ISO 4217). Defaults to USD. | [optional] 
 **var_from** | **str**| Window start YYYY-MM-DD (UTC). Defaults to ~2 years before &#x60;to&#x60;. | [optional] 
 **to** | **str**| Window end YYYY-MM-DD (UTC). Defaults to today. | [optional] 
 **limit** | **float**| How many to return (default 10, max 50). | [optional] 

### Return type

[**MeanReversionResponse**](MeanReversionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Requires the growth plan or higher. |  -  |
**429** | Rate limit or monthly quota exceeded. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ppp_analysis**
> PppAnalysisResponse ppp_analysis(countries=countries, var_from=var_from, to=to, period=period, sort=sort, limit=limit, stats=stats)

PPP analysis

PPP over time: how a country's purchasing-power-parity factor changed, comparing countries, or 'movers'. Growth plan or higher.

### Example

* Bearer Authentication (bearerAuth):

```python
import currencycore
from currencycore.models.ppp_analysis_response import PppAnalysisResponse
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = currencycore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)
    countries = 'IND,DEU,USA' # str | Comma-separated ISO 3166-1 alpha-3 country codes to compare, e.g. IND,DEU,USA. OMIT to rank ALL countries by PPP-factor change ('movers' mode). (optional)
    var_from = 'var_from_example' # str | Window start YEAR (e.g. 2015). Defaults to 10 years before `to`. See `period` for a shorthand. (optional)
    to = 'to_example' # str | Window end YEAR (e.g. 2024). Defaults to the current year. (optional)
    period = '10y' # str | Relative window shorthand for `from`: e.g. 10y, 20y, max. Ignored if `from` is given. (optional)
    sort = 'increased' # str | Movers ranking: increased (PPP factor rose most, default) or decreased. (optional)
    limit = 10 # float | Movers: how many top results to return (default 10, max 200). (optional)
    stats = true # bool | Include min/max/avg of the PPP factor over the window per country. Defaults to true; pass false to skip. (optional)

    try:
        # PPP analysis
        api_response = api_instance.ppp_analysis(countries=countries, var_from=var_from, to=to, period=period, sort=sort, limit=limit, stats=stats)
        print("The response of CurrencyCoreApi->ppp_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->ppp_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countries** | **str**| Comma-separated ISO 3166-1 alpha-3 country codes to compare, e.g. IND,DEU,USA. OMIT to rank ALL countries by PPP-factor change (&#39;movers&#39; mode). | [optional] 
 **var_from** | **str**| Window start YEAR (e.g. 2015). Defaults to 10 years before &#x60;to&#x60;. See &#x60;period&#x60; for a shorthand. | [optional] 
 **to** | **str**| Window end YEAR (e.g. 2024). Defaults to the current year. | [optional] 
 **period** | **str**| Relative window shorthand for &#x60;from&#x60;: e.g. 10y, 20y, max. Ignored if &#x60;from&#x60; is given. | [optional] 
 **sort** | **str**| Movers ranking: increased (PPP factor rose most, default) or decreased. | [optional] 
 **limit** | **float**| Movers: how many top results to return (default 10, max 200). | [optional] 
 **stats** | **bool**| Include min/max/avg of the PPP factor over the window per country. Defaults to true; pass false to skip. | [optional] 

### Return type

[**PppAnalysisResponse**](PppAnalysisResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Requires the growth plan or higher. |  -  |
**429** | Rate limit or monthly quota exceeded. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rates**
> RatesResponse rates(var_date=var_date)

Rates

The full exchange-rate snapshot for a date (USD base).

### Example

* Bearer Authentication (bearerAuth):

```python
import currencycore
from currencycore.models.rates_response import RatesResponse
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = currencycore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)
    var_date = 'var_date_example' # str | YYYY-MM-DD. Defaults to the latest available date. (optional)

    try:
        # Rates
        api_response = api_instance.rates(var_date=var_date)
        print("The response of CurrencyCoreApi->rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| YYYY-MM-DD. Defaults to the latest available date. | [optional] 

### Return type

[**RatesResponse**](RatesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**429** | Rate limit or monthly quota exceeded. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rates_by_base**
> RatesByBaseResponse rates_by_base(base, var_date=var_date)

Rates by base

The same snapshot re-expressed against any base currency.

### Example

* Bearer Authentication (bearerAuth):

```python
import currencycore
from currencycore.models.rates_by_base_response import RatesByBaseResponse
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = currencycore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)
    base = 'EUR' # str | Base currency (3-letter ISO 4217), e.g. EUR.
    var_date = 'var_date_example' # str | YYYY-MM-DD. Defaults to the latest available date. (optional)

    try:
        # Rates by base
        api_response = api_instance.rates_by_base(base, var_date=var_date)
        print("The response of CurrencyCoreApi->rates_by_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->rates_by_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base** | **str**| Base currency (3-letter ISO 4217), e.g. EUR. | 
 **var_date** | **str**| YYYY-MM-DD. Defaults to the latest available date. | [optional] 

### Return type

[**RatesByBaseResponse**](RatesByBaseResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**429** | Rate limit or monthly quota exceeded. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **safe_haven**
> SafeHavenResponse safe_haven(currencies=currencies, base=base, var_from=var_from, to=to, limit=limit)

Safe haven

Ranks currencies by a composite safe-haven score (low volatility + shallow drawdown + 2008-crisis resilience). Growth plan or higher.

### Example

* Bearer Authentication (bearerAuth):

```python
import currencycore
from currencycore.models.safe_haven_response import SafeHavenResponse
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = currencycore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)
    currencies = 'CHF,JPY' # str | Comma-separated currencies to score, e.g. CHF,JPY. OMIT to rank the safe-haven pool (includes gold). (optional)
    base = 'USD' # str | Base currency to measure against (3-letter ISO 4217). Defaults to USD. (optional)
    var_from = 'var_from_example' # str | Window start YYYY-MM-DD (UTC). Defaults to 2007-01-01 (spans the 2008 crisis + COVID). (optional)
    to = 'to_example' # str | Window end YYYY-MM-DD (UTC). Defaults to today. (optional)
    limit = 10 # float | How many to return (default 10, max 50). (optional)

    try:
        # Safe haven
        api_response = api_instance.safe_haven(currencies=currencies, base=base, var_from=var_from, to=to, limit=limit)
        print("The response of CurrencyCoreApi->safe_haven:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->safe_haven: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencies** | **str**| Comma-separated currencies to score, e.g. CHF,JPY. OMIT to rank the safe-haven pool (includes gold). | [optional] 
 **base** | **str**| Base currency to measure against (3-letter ISO 4217). Defaults to USD. | [optional] 
 **var_from** | **str**| Window start YYYY-MM-DD (UTC). Defaults to 2007-01-01 (spans the 2008 crisis + COVID). | [optional] 
 **to** | **str**| Window end YYYY-MM-DD (UTC). Defaults to today. | [optional] 
 **limit** | **float**| How many to return (default 10, max 50). | [optional] 

### Return type

[**SafeHavenResponse**](SafeHavenResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Requires the growth plan or higher. |  -  |
**429** | Rate limit or monthly quota exceeded. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volatility**
> VolatilityResponse volatility(currency=currency, base=base, var_from=var_from, to=to, sort=sort, universe=universe, limit=limit)

Volatility

Annualized volatility of a currency vs a base, or a stability ranking of the liquid currencies. Growth plan or higher.

### Example

* Bearer Authentication (bearerAuth):

```python
import currencycore
from currencycore.models.volatility_response import VolatilityResponse
from currencycore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.currency-core.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = currencycore.Configuration(
    host = "https://api.currency-core.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = currencycore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with currencycore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencycore.CurrencyCoreApi(api_client)
    currency = 'EUR' # str | Currency to measure (3-letter ISO 4217), or a comma-separated list to compare. OMIT to RANK the liquid-currency set by stability. (optional)
    base = 'USD' # str | Base currency to measure against (3-letter ISO 4217). Defaults to USD. (optional)
    var_from = 'var_from_example' # str | Window start YYYY-MM-DD (UTC). Defaults to 365 days before `to`. (optional)
    to = 'to_example' # str | Window end YYYY-MM-DD (UTC). Defaults to today; a future date clamps to today. (optional)
    sort = 'stable' # str | Ranking direction: stable (least volatile first, default) or volatile. (optional)
    universe = 'liquid' # str | Ranking universe: liquid (default, broad set) or majors (USD/EUR/GBP/JPY/CHF/CAD/AUD/NZD). Use majors for 'most volatile major pair'. (optional)
    limit = 10 # float | Ranking: how many to return (default 10, max 50). (optional)

    try:
        # Volatility
        api_response = api_instance.volatility(currency=currency, base=base, var_from=var_from, to=to, sort=sort, universe=universe, limit=limit)
        print("The response of CurrencyCoreApi->volatility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyCoreApi->volatility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency to measure (3-letter ISO 4217), or a comma-separated list to compare. OMIT to RANK the liquid-currency set by stability. | [optional] 
 **base** | **str**| Base currency to measure against (3-letter ISO 4217). Defaults to USD. | [optional] 
 **var_from** | **str**| Window start YYYY-MM-DD (UTC). Defaults to 365 days before &#x60;to&#x60;. | [optional] 
 **to** | **str**| Window end YYYY-MM-DD (UTC). Defaults to today; a future date clamps to today. | [optional] 
 **sort** | **str**| Ranking direction: stable (least volatile first, default) or volatile. | [optional] 
 **universe** | **str**| Ranking universe: liquid (default, broad set) or majors (USD/EUR/GBP/JPY/CHF/CAD/AUD/NZD). Use majors for &#39;most volatile major pair&#39;. | [optional] 
 **limit** | **float**| Ranking: how many to return (default 10, max 50). | [optional] 

### Return type

[**VolatilityResponse**](VolatilityResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Invalid or missing request parameters. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Requires the growth plan or higher. |  -  |
**429** | Rate limit or monthly quota exceeded. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

