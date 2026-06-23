# HistoryAnalysisResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** |  | 
**var_from** | **str** |  | 
**to** | **str** |  | 
**mode** | **str** |  | 
**sort** | **str** |  | [optional] 
**asset_class** | **str** |  | [optional] 
**interval** | **str** |  | [optional] 
**stats** | **bool** |  | 
**results** | [**List[HistoryAnalysisResponseResultsInner]**](HistoryAnalysisResponseResultsInner.md) |  | 

## Example

```python
from currencycore.models.history_analysis_response import HistoryAnalysisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryAnalysisResponse from a JSON string
history_analysis_response_instance = HistoryAnalysisResponse.from_json(json)
# print the JSON string representation of the object
print(HistoryAnalysisResponse.to_json())

# convert the object into a dict
history_analysis_response_dict = history_analysis_response_instance.to_dict()
# create an instance of HistoryAnalysisResponse from a dict
history_analysis_response_from_dict = HistoryAnalysisResponse.from_dict(history_analysis_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


