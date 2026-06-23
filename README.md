# CurrencyCore SDK for Python

Official client for the [CurrencyCore](https://currency-core.com) API — currency
conversion, FX rates, PPP, and analytics.

Generated from the CurrencyCore OpenAPI 3.1 spec with
[OpenAPI Generator](https://openapi-generator.tech) (`python`, urllib3), plus a
thin `create_client` helper for API-key and version handling.

## Install

```bash
pip install currencycore
```

## Quickstart

```python
from currencycore.client import create_client

api = create_client(api_key="cc_live_...")  # or set CURRENCYCORE_API_KEY
res = api.convert(var_from="USD", to="EUR", amount=100)
print(res.results[0])
```

`var_from` carries the `var_` prefix because `from` is a reserved word in Python.

Public reference endpoints need no key:

```python
api = create_client()
print(api.currencies())
```

## API key

`create_client` resolves the key as `api_key` → `CURRENCYCORE_API_KEY`.

## API version

Base URL is `https://api.currency-core.com/{version}` (default `v1`):

```python
create_client(version="v1")
create_client(base_url="https://api.currency-core.com/v1")
```

## Low-level client

```python
import currencycore

config = currencycore.Configuration(
    host="https://api.currency-core.com/v1", access_token="cc_live_..."
)
api = currencycore.CurrencyCoreApi(currencycore.ApiClient(config))
```

## Regenerate

The committed `openapi.json` is the source of truth:

```bash
bash scripts/generate.sh
```

Hand-written files (`currencycore/client.py`, this README) are protected by
`.openapi-generator-ignore`.

## License

MIT
