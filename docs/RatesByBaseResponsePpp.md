# RatesByBaseResponsePpp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** |  | 
**year** | **float** |  | 
**values** | **Dict[str, float]** |  | 

## Example

```python
from currencycore.models.rates_by_base_response_ppp import RatesByBaseResponsePpp

# TODO update the JSON string below
json = "{}"
# create an instance of RatesByBaseResponsePpp from a JSON string
rates_by_base_response_ppp_instance = RatesByBaseResponsePpp.from_json(json)
# print the JSON string representation of the object
print(RatesByBaseResponsePpp.to_json())

# convert the object into a dict
rates_by_base_response_ppp_dict = rates_by_base_response_ppp_instance.to_dict()
# create an instance of RatesByBaseResponsePpp from a dict
rates_by_base_response_ppp_from_dict = RatesByBaseResponsePpp.from_dict(rates_by_base_response_ppp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


