# ConvertResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | 
**to_country** | **str** |  | [optional] 
**result** | **float** |  | 
**rate** | **float** |  | 
**ppp** | [**ConvertResponseResultsInnerPpp**](ConvertResponseResultsInnerPpp.md) |  | [optional] 

## Example

```python
from currencycore.models.convert_response_results_inner import ConvertResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertResponseResultsInner from a JSON string
convert_response_results_inner_instance = ConvertResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(ConvertResponseResultsInner.to_json())

# convert the object into a dict
convert_response_results_inner_dict = convert_response_results_inner_instance.to_dict()
# create an instance of ConvertResponseResultsInner from a dict
convert_response_results_inner_from_dict = ConvertResponseResultsInner.from_dict(convert_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


