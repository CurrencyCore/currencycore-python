# CurrenciesResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**numeric** | **str** |  | 
**name** | **str** |  | 
**symbol** | **str** |  | 

## Example

```python
from currencycore.models.currencies_response_inner import CurrenciesResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CurrenciesResponseInner from a JSON string
currencies_response_inner_instance = CurrenciesResponseInner.from_json(json)
# print the JSON string representation of the object
print(CurrenciesResponseInner.to_json())

# convert the object into a dict
currencies_response_inner_dict = currencies_response_inner_instance.to_dict()
# create an instance of CurrenciesResponseInner from a dict
currencies_response_inner_from_dict = CurrenciesResponseInner.from_dict(currencies_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


