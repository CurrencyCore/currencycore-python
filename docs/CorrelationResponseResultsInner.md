# CorrelationResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**correlation** | **float** |  | 
**observations** | **float** |  | 
**note** | **str** |  | [optional] 

## Example

```python
from currencycore.models.correlation_response_results_inner import CorrelationResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CorrelationResponseResultsInner from a JSON string
correlation_response_results_inner_instance = CorrelationResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(CorrelationResponseResultsInner.to_json())

# convert the object into a dict
correlation_response_results_inner_dict = correlation_response_results_inner_instance.to_dict()
# create an instance of CorrelationResponseResultsInner from a dict
correlation_response_results_inner_from_dict = CorrelationResponseResultsInner.from_dict(correlation_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


