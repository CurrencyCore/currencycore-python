# SafeHavenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** |  | 
**var_from** | **str** |  | 
**to** | **str** |  | 
**crisis** | [**SafeHavenResponseCrisis**](SafeHavenResponseCrisis.md) |  | 
**universe** | **str** |  | [optional] 
**results** | [**List[SafeHavenResponseResultsInner]**](SafeHavenResponseResultsInner.md) |  | 

## Example

```python
from currencycore.models.safe_haven_response import SafeHavenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SafeHavenResponse from a JSON string
safe_haven_response_instance = SafeHavenResponse.from_json(json)
# print the JSON string representation of the object
print(SafeHavenResponse.to_json())

# convert the object into a dict
safe_haven_response_dict = safe_haven_response_instance.to_dict()
# create an instance of SafeHavenResponse from a dict
safe_haven_response_from_dict = SafeHavenResponse.from_dict(safe_haven_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


