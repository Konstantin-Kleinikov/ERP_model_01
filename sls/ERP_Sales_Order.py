"""Module for handling of sales orders."""
from __future__ import annotations
from datetime import datetime as dt

from com.ERP_Document import Document
from com.ERP_Business_Partner import Customer


class SalesOrder(Document):
    DOCUMENT_TYPE = 'Sales Order'
    FUNCTIONAL_DOMAIN = 'Logistic'

    def __init__(self, business_entity: int, customer: Customer, order_date: str, currency: str, amount: float) -> None:
        self.order_date = dt.strptime(order_date, '%d-%m-%Y').date()
        self.doc_type = SalesOrder.DOCUMENT_TYPE
        self.numbering_prefix = 'SLS'
        super().__init__(business_entity, currency, amount, self.order_date, self.numbering_prefix)
        self.order_amount = amount
        self.funct_domain = SalesOrder.FUNCTIONAL_DOMAIN
        self.customer = customer

    def __repr__(self):
        return f'Sales Order: {self.__dict__}'

    def copy_sales_order(self) -> SalesOrder:
        # Convert order date from dt.date to string
        order_date = dt.strftime(self.order_date, '%d-%m-%Y')
        # Create new sales order object based on data of existing sales order
        return SalesOrder(self.business_entity,
                          self.customer,
                          order_date,
                          self.currency,
                          self.order_amount
                          )
