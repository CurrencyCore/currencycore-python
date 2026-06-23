# CountriesResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** |  | 
**currencies** | **List[str]** |  | [optional] 

## Example

```python
from currencycore.models.countries_response_inner import CountriesResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CountriesResponseInner from a JSON string
countries_response_inner_instance = CountriesResponseInner.from_json(json)
# print the JSON string representation of the object
print(CountriesResponseInner.to_json())

# convert the object into a dict
countries_response_inner_dict = countries_response_inner_instance.to_dict()
# create an instance of CountriesResponseInner from a dict
countries_response_inner_from_dict = CountriesResponseInner.from_dict(countries_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


