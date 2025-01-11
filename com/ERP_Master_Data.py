"""Master data for ERP objects handling"""
from datetime import date
from decimal import Decimal, getcontext
from typing import Optional



CSV_DELIMITER = '~'
# Business units
business_entities = {101: [{'name': 'ОАО "Крупно и гладко"', 'local_currency': 'RUB'}],
                     201: [{'name': 'JS Cold & Freeze Equipment', 'local_currency': 'EUR'}]
                     }

# Currency rates
local_currency_rates = {'EUR': [{'2024-01-01': '99.1919',
                                 '2024-12-06': '109.7802',
                                 '2024-06-01': '97.7908',
                                 '2025-01-10': '105.0893'}
                                ],
                        'USD': [{'2024-01-01': '89.6883',
                                 '2024-12-06': '103.3837',
                                 '2024-06-01': '90.1915',
                                 '2025-01-10': '102.2911'}

                                ]

                        }
# Business-partners

# Items

# Precision for Decimal calculations (currency rates)
getcontext().prec = 5

# FUNCTION SECTION

def calculate_currency_rate(currency: str, doc_date: Optional[date]=None) -> Optional[Decimal]:
    """
    Searches for currency rate that is effective at document date.

    If document date is not specified, the current system date is used to search the currency rate.

    :param currency: str, currency code, e.g. 'EUR', 'RUB', etc.
    :param doc_date: date, document date

    :return: currency rate or None if currency rate is not found for currency and doc_date
    """
    document_date = (date.strftime(doc_date, '%Y-%m-%d')
                if doc_date
                else date.strftime(date.today(), '%Y-%m-%d')
                )
    # Use a "list comprehension" for getting the list of rate dates that are earlier or equal to doc_date,
    # sorted ascending.
    rate_dates = sorted([rate_date
                         for rate_date
                         in local_currency_rates[currency][0]
                         if rate_date <= document_date]
                        )
    # Get the last rate date in the list of rate_dates
    last_rate_date = rate_dates[-1:]
    try:
        currency_rate = Decimal(local_currency_rates[currency][0][last_rate_date[0]])
    except IndexError:
        # Currency rate for currency {currency} on document date {document_date} not found.
        return None
    else:
        print(f'Currency rate for currency {currency} on date {last_rate_date} is {currency_rate}')
        return currency_rate
