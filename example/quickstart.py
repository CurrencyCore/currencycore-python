import os

from currencycore.client import create_client


def main() -> None:
    api = create_client(api_key=os.environ.get("CURRENCYCORE_API_KEY"))

    # `var_from` because `from` is a reserved word in Python.
    converted = api.convert(var_from="USD", to="EUR", amount=100)
    print("100 USD =", converted.results[0])

    # Public endpoint, no key required.
    currencies = api.currencies()
    print("supported currencies:", len(currencies))


if __name__ == "__main__":
    main()
