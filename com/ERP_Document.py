"""Module for generic ERP Document objects"""
from datetime import datetime as dt, date
from decimal import Decimal, getcontext
from typing import Optional

from com.ERP_Object import ErpObject
import com.ERP_Master_Data

# Precision of rounding amounts
ROUND_AMOUNTS = 2

last_used_doc_numbers: dict[str, int] = {'GEN': 0, 'FIN': 0, 'SLS': 0}

# Precision for Decimal calculations (currency rates)
getcontext().prec = 5



class Document(ErpObject):
    def __init__(self, business_entity: int,
                 doc_currency: str,  # document currency
                 amount: float,  # amount in document currency
                 doc_date: Optional[date]=None,
                 numbering_prefix: Optional[str]=None
                 ) -> None:
        super().__init__(numbering_prefix)
        self.business_entity = business_entity
        self.verify_currency(doc_currency)
        self.currency = doc_currency
        self.local_currency = com.ERP_Master_Data.business_entities[business_entity][0]['local_currency']
        self.date_created = dt.now().date()
        # Get currency rate and calculate amount in local currency if document currency differs from local currency.
        if self.currency != self.local_currency:
            self.currency_rate, self.local_currency_amount = (self.calculate_currency_amount(doc_currency,
                                                                                             amount,
                                                                                             doc_date
                                                                                             )
                                                              )
        else:
            self.currency_rate = 1
            self.local_currency_amount = amount


    @classmethod
    def verify_currency(cls, currency):
        # TODO, verify that currency code exists
        pass

    @staticmethod
    def calculate_currency_amount(currency: str, amount: float, doc_date: Optional[date]=None) -> tuple:
        """Calculate amount in local currency using the rate, effective at document date.

        Currency ISO code and amount are required. If document date is not specified, the current date is
        used to search the currency rate.

        :param currency: str, currency code, e.g. 'EUR', 'RUB', etc.
        :param amount: float, amount in specified currency
        :param doc_date: date, document date that is used to search for currency rate

        :returns: tuple currency_rate, local_currency_amount
        """
        # Calculate amount in foreign currency
        currency_rate = None
        local_currency_amount = 0.00
        if doc_date:
            currency_rate = com.ERP_Master_Data.calculate_currency_rate(currency, doc_date)
            if currency_rate:
                local_currency_amount = round(float(Decimal(str(amount)) * currency_rate), ROUND_AMOUNTS)
        return currency_rate, local_currency_amount
