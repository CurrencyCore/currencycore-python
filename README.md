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

## Endpoints

All 14 endpoints are methods on the `api` client. `*` marks a required argument; the rest are optional. `from`/`date` become `var_from`/`var_date` (reserved words). **Public** = no key; **Free** = any plan with a key; **Growth** = Growth plan or higher.

| Endpoint | Call | Plan |
| --- | --- | --- |
| Convert an amount (optional PPP) | `api.convert(var_from*, to*, amount, ppp, var_date)` | Free |
| Rate snapshot for a date (USD base) | `api.rates(var_date)` | Free |
| Rate snapshot in any base | `api.rates_by_base(base*, var_date)` | Free |
| One currency's daily time series | `api.history(currency*, var_from, to, base, interval)` | Growth |
| Trends, comparisons & movers | `api.history_analysis(base, currencies, var_from, to, period, sort, asset_class, limit, interval, stats)` | Growth |
| PPP factor over time / movers | `api.ppp_analysis(countries, var_from, to, period, sort, limit, stats)` | Growth |
| Volatility or stability ranking | `api.volatility(currency, base, var_from, to, sort, universe, limit)` | Growth |
| Return correlation vs a base | `api.correlation(currencies*, base, var_from, to)` | Growth |
| Max drawdown or ranking | `api.drawdown(currency, base, var_from, to, sort, universe, limit)` | Growth |
| Safe-haven score ranking | `api.safe_haven(currencies, base, var_from, to, limit)` | Growth |
| Mean-reversion ranking | `api.mean_reversion(currencies, base, var_from, to, limit)` | Growth |
| Supported countries + currencies | `api.countries()` | Public |
| Supported ISO 4217 currencies | `api.currencies()` | Public |
| Natural-language question | `api.ai(q*)` | Free |

More calls:

```python
api.rates()                                          # latest snapshot (USD base)
api.rates_by_base(base="EUR")                        # same snapshot, EUR base
api.history(currency="INR", var_from="2024-01-01")
api.volatility(universe="majors", sort="volatile")   # most-volatile majors
api.ai(q="How has the rupee moved this year?")
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
