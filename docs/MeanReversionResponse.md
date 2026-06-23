# MeanReversionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** |  | 
**var_from** | **str** |  | 
**to** | **str** |  | 
**universe** | **str** |  | [optional] 
**results** | [**List[MeanReversionResponseResultsInner]**](MeanReversionResponseResultsInner.md) |  | 

## Example

```python
from currencycore.models.mean_reversion_response import MeanReversionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MeanReversionResponse from a JSON string
mean_reversion_response_instance = MeanReversionResponse.from_json(json)
# print the JSON string representation of the object
print(MeanReversionResponse.to_json())

# convert the object into a dict
mean_reversion_response_dict = mean_reversion_response_instance.to_dict()
# create an instance of MeanReversionResponse from a dict
mean_reversion_response_from_dict = MeanReversionResponse.from_dict(mean_reversion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


