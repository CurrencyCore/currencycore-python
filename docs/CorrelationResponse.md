# CorrelationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** |  | 
**var_from** | **str** |  | 
**to** | **str** |  | 
**results** | [**List[CorrelationResponseResultsInner]**](CorrelationResponseResultsInner.md) |  | 

## Example

```python
from currencycore.models.correlation_response import CorrelationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CorrelationResponse from a JSON string
correlation_response_instance = CorrelationResponse.from_json(json)
# print the JSON string representation of the object
print(CorrelationResponse.to_json())

# convert the object into a dict
correlation_response_dict = correlation_response_instance.to_dict()
# create an instance of CorrelationResponse from a dict
correlation_response_from_dict = CorrelationResponse.from_dict(correlation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


