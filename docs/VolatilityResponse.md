# VolatilityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** |  | 
**var_from** | **str** |  | 
**to** | **str** |  | 
**mode** | **str** |  | 
**sort** | **str** |  | [optional] 
**universe** | **str** |  | [optional] 
**basis** | **str** |  | 
**results** | [**List[VolatilityResponseResultsInner]**](VolatilityResponseResultsInner.md) |  | 

## Example

```python
from currencycore.models.volatility_response import VolatilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VolatilityResponse from a JSON string
volatility_response_instance = VolatilityResponse.from_json(json)
# print the JSON string representation of the object
print(VolatilityResponse.to_json())

# convert the object into a dict
volatility_response_dict = volatility_response_instance.to_dict()
# create an instance of VolatilityResponse from a dict
volatility_response_from_dict = VolatilityResponse.from_dict(volatility_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


