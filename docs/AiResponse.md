# AiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**answer** | **str** |  | 
**data** | **List[object]** |  | 
**tool_calls** | **float** |  | [optional] 

## Example

```python
from currencycore.models.ai_response import AiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AiResponse from a JSON string
ai_response_instance = AiResponse.from_json(json)
# print the JSON string representation of the object
print(AiResponse.to_json())

# convert the object into a dict
ai_response_dict = ai_response_instance.to_dict()
# create an instance of AiResponse from a dict
ai_response_from_dict = AiResponse.from_dict(ai_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


