# PppAnalysisResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **float** |  | 
**to** | **float** |  | 
**mode** | **str** |  | 
**sort** | **str** |  | [optional] 
**stats** | **bool** |  | 
**results** | [**List[PppAnalysisResponseResultsInner]**](PppAnalysisResponseResultsInner.md) |  | 

## Example

```python
from currencycore.models.ppp_analysis_response import PppAnalysisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PppAnalysisResponse from a JSON string
ppp_analysis_response_instance = PppAnalysisResponse.from_json(json)
# print the JSON string representation of the object
print(PppAnalysisResponse.to_json())

# convert the object into a dict
ppp_analysis_response_dict = ppp_analysis_response_instance.to_dict()
# create an instance of PppAnalysisResponse from a dict
ppp_analysis_response_from_dict = PppAnalysisResponse.from_dict(ppp_analysis_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


