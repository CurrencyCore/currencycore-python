# DrawdownResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** |  | 
**var_from** | **str** |  | 
**to** | **str** |  | 
**mode** | **str** |  | 
**sort** | **str** |  | [optional] 
**universe** | **str** |  | [optional] 
**results** | [**List[DrawdownResponseResultsInner]**](DrawdownResponseResultsInner.md) |  | 

## Example

```python
from currencycore.models.drawdown_response import DrawdownResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DrawdownResponse from a JSON string
drawdown_response_instance = DrawdownResponse.from_json(json)
# print the JSON string representation of the object
print(DrawdownResponse.to_json())

# convert the object into a dict
drawdown_response_dict = drawdown_response_instance.to_dict()
# create an instance of DrawdownResponse from a dict
drawdown_response_from_dict = DrawdownResponse.from_dict(drawdown_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


