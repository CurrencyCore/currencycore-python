# RatesByBaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** |  | 
**var_date** | **str** |  | 
**requested_date** | **str** |  | [optional] 
**as_of** | **Dict[str, str]** |  | [optional] 
**rates** | **Dict[str, float]** |  | 
**ppp** | [**RatesByBaseResponsePpp**](RatesByBaseResponsePpp.md) |  | [optional] 

## Example

```python
from currencycore.models.rates_by_base_response import RatesByBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RatesByBaseResponse from a JSON string
rates_by_base_response_instance = RatesByBaseResponse.from_json(json)
# print the JSON string representation of the object
print(RatesByBaseResponse.to_json())

# convert the object into a dict
rates_by_base_response_dict = rates_by_base_response_instance.to_dict()
# create an instance of RatesByBaseResponse from a dict
rates_by_base_response_from_dict = RatesByBaseResponse.from_dict(rates_by_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


