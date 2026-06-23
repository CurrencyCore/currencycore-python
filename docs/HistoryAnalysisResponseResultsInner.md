# HistoryAnalysisResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**start_date** | **str** |  | 
**end_date** | **str** |  | 
**start_rate** | **float** |  | 
**end_rate** | **float** |  | 
**change_pct** | **float** |  | 
**strengthened_pct** | **float** |  | 
**stats** | [**HistoryAnalysisResponseResultsInnerStats**](HistoryAnalysisResponseResultsInnerStats.md) |  | [optional] 
**series** | **Dict[str, float]** |  | [optional] 
**volatility** | **float** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from currencycore.models.history_analysis_response_results_inner import HistoryAnalysisResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryAnalysisResponseResultsInner from a JSON string
history_analysis_response_results_inner_instance = HistoryAnalysisResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(HistoryAnalysisResponseResultsInner.to_json())

# convert the object into a dict
history_analysis_response_results_inner_dict = history_analysis_response_results_inner_instance.to_dict()
# create an instance of HistoryAnalysisResponseResultsInner from a dict
history_analysis_response_results_inner_from_dict = HistoryAnalysisResponseResultsInner.from_dict(history_analysis_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


