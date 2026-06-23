# SafeHavenResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**score** | **float** |  | 
**volatility** | **float** |  | 
**max_drawdown_pct** | **float** |  | 
**crisis_return_pct** | **float** |  | 
**note** | **str** |  | [optional] 

## Example

```python
from currencycore.models.safe_haven_response_results_inner import SafeHavenResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SafeHavenResponseResultsInner from a JSON string
safe_haven_response_results_inner_instance = SafeHavenResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(SafeHavenResponseResultsInner.to_json())

# convert the object into a dict
safe_haven_response_results_inner_dict = safe_haven_response_results_inner_instance.to_dict()
# create an instance of SafeHavenResponseResultsInner from a dict
safe_haven_response_results_inner_from_dict = SafeHavenResponseResultsInner.from_dict(safe_haven_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


