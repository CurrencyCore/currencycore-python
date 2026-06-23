# ConvertResponseResultsInnerPpp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_factor** | **float** |  | 
**to_factor** | **float** |  | 
**result** | **float** |  | 
**year** | **float** |  | 
**source** | **str** |  | 
**error** | **str** |  | 

## Example

```python
from currencycore.models.convert_response_results_inner_ppp import ConvertResponseResultsInnerPpp

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertResponseResultsInnerPpp from a JSON string
convert_response_results_inner_ppp_instance = ConvertResponseResultsInnerPpp.from_json(json)
# print the JSON string representation of the object
print(ConvertResponseResultsInnerPpp.to_json())

# convert the object into a dict
convert_response_results_inner_ppp_dict = convert_response_results_inner_ppp_instance.to_dict()
# create an instance of ConvertResponseResultsInnerPpp from a dict
convert_response_results_inner_ppp_from_dict = ConvertResponseResultsInnerPpp.from_dict(convert_response_results_inner_ppp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


