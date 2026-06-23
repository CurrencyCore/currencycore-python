# SafeHavenResponseCrisis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**var_from** | **str** |  | 
**to** | **str** |  | 

## Example

```python
from currencycore.models.safe_haven_response_crisis import SafeHavenResponseCrisis

# TODO update the JSON string below
json = "{}"
# create an instance of SafeHavenResponseCrisis from a JSON string
safe_haven_response_crisis_instance = SafeHavenResponseCrisis.from_json(json)
# print the JSON string representation of the object
print(SafeHavenResponseCrisis.to_json())

# convert the object into a dict
safe_haven_response_crisis_dict = safe_haven_response_crisis_instance.to_dict()
# create an instance of SafeHavenResponseCrisis from a dict
safe_haven_response_crisis_from_dict = SafeHavenResponseCrisis.from_dict(safe_haven_response_crisis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


