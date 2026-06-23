# DrawdownResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**max_drawdown_pct** | **float** |  | 
**peak_date** | **str** |  | [optional] 
**trough_date** | **str** |  | [optional] 
**recovery_date** | **str** |  | [optional] 
**recovery_days** | **float** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from currencycore.models.drawdown_response_results_inner import DrawdownResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DrawdownResponseResultsInner from a JSON string
drawdown_response_results_inner_instance = DrawdownResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(DrawdownResponseResultsInner.to_json())

# convert the object into a dict
drawdown_response_results_inner_dict = drawdown_response_results_inner_instance.to_dict()
# create an instance of DrawdownResponseResultsInner from a dict
drawdown_response_results_inner_from_dict = DrawdownResponseResultsInner.from_dict(drawdown_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


