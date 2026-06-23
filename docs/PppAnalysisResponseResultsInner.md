# PppAnalysisResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**start_year** | **float** |  | 
**end_year** | **float** |  | 
**start_factor** | **float** |  | 
**end_factor** | **float** |  | 
**change_pct** | **float** |  | 
**projected** | **bool** |  | 
**stats** | [**HistoryAnalysisResponseResultsInnerStats**](HistoryAnalysisResponseResultsInnerStats.md) |  | [optional] 
**series** | **Dict[str, float]** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from currencycore.models.ppp_analysis_response_results_inner import PppAnalysisResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PppAnalysisResponseResultsInner from a JSON string
ppp_analysis_response_results_inner_instance = PppAnalysisResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(PppAnalysisResponseResultsInner.to_json())

# convert the object into a dict
ppp_analysis_response_results_inner_dict = ppp_analysis_response_results_inner_instance.to_dict()
# create an instance of PppAnalysisResponseResultsInner from a dict
ppp_analysis_response_results_inner_from_dict = PppAnalysisResponseResultsInner.from_dict(ppp_analysis_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


