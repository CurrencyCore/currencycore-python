# RatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**base** | **str** |  | 
**rates** | **Dict[str, float]** |  | 
**requested_date** | **str** |  | [optional] 
**as_of** | **Dict[str, str]** |  | [optional] 

## Example

```python
from currencycore.models.rates_response import RatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RatesResponse from a JSON string
rates_response_instance = RatesResponse.from_json(json)
# print the JSON string representation of the object
print(RatesResponse.to_json())

# convert the object into a dict
rates_response_dict = rates_response_instance.to_dict()
# create an instance of RatesResponse from a dict
rates_response_from_dict = RatesResponse.from_dict(rates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


