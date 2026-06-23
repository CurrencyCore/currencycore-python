"""Environment-aware client factory layered on the generated client."""
from __future__ import annotations

import os
from typing import Optional

import currencycore

DEFAULT_HOST = "https://api.currency-core.com"


def create_client(
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    version: str = "v1",
) -> currencycore.CurrencyCoreApi:
    """Build a :class:`currencycore.CurrencyCoreApi`.

    Resolves the API key as ``api_key`` -> ``CURRENCYCORE_API_KEY`` and the base
    URL as ``base_url`` -> ``CURRENCYCORE_BASE_URL`` -> the public host with
    ``version``. Omit the key for the public reference endpoints.
    """
    api_key = api_key or os.environ.get("CURRENCYCORE_API_KEY")
    host = base_url or os.environ.get("CURRENCYCORE_BASE_URL") or f"{DEFAULT_HOST}/{version}"
    config = currencycore.Configuration(host=host, access_token=api_key)
    return currencycore.CurrencyCoreApi(currencycore.ApiClient(config))
