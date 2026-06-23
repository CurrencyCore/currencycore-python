# VolatilityResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**volatility** | **float** |  | 
**observations** | **float** |  | 
**note** | **str** |  | [optional] 

## Example

```python
from currencycore.models.volatility_response_results_inner import VolatilityResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of VolatilityResponseResultsInner from a JSON string
volatility_response_results_inner_instance = VolatilityResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(VolatilityResponseResultsInner.to_json())

# convert the object into a dict
volatility_response_results_inner_dict = volatility_response_results_inner_instance.to_dict()
# create an instance of VolatilityResponseResultsInner from a dict
volatility_response_results_inner_from_dict = VolatilityResponseResultsInner.from_dict(volatility_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


