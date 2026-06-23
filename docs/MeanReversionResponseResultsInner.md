# MeanReversionResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**score** | **float** |  | 
**deviation_pct** | **float** |  | 
**reversion_frequency** | **float** |  | 
**half_life_days** | **float** |  | 
**note** | **str** |  | [optional] 

## Example

```python
from currencycore.models.mean_reversion_response_results_inner import MeanReversionResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MeanReversionResponseResultsInner from a JSON string
mean_reversion_response_results_inner_instance = MeanReversionResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(MeanReversionResponseResultsInner.to_json())

# convert the object into a dict
mean_reversion_response_results_inner_dict = mean_reversion_response_results_inner_instance.to_dict()
# create an instance of MeanReversionResponseResultsInner from a dict
mean_reversion_response_results_inner_from_dict = MeanReversionResponseResultsInner.from_dict(mean_reversion_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


