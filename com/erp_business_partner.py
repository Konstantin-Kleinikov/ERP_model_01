"""Module for handling of business-partners"""
from com.erp_object import ErpObject

business_partners = {'SUP000000001': [{'name': 'JSC "Powerful engines"', 'tax_id': 9729219090}],
                     'CUS000000001': [{'name': 'Doo "Sinaps"', 'tax_id': 9729219089}]
                     }


class BusinessPartner(ErpObject):

    def __init__(self, bp_name: str, bp_tax_id: int, numbering_prefix):
        super().__init__(numbering_prefix)
        self.name = bp_name
        self.tax_id = bp_tax_id

    @property
    def tax_id(self):
        return self.__tax_id

    @tax_id.setter
    def tax_id(self, bp_tax_id):
        # TODO Verify tax_id method
        self.__tax_id = bp_tax_id


class Supplier(BusinessPartner):

    def __init__(self, bp_name: str, bp_tax_id: int, lead_time: float):
        self.numbering_prefix = 'SUP'
        super().__init__(bp_name, bp_tax_id, self.numbering_prefix)
        self.lead_time = (lead_time, 'days')
        self.purchase_office = 'PUR-010'
        ErpObject.write_object_to_csv(self)


class Customer(BusinessPartner):

    def __init__(self, bp_name: str, bp_tax_id: int):
        self.numbering_prefix = 'CUS'
        super().__init__(bp_name, bp_tax_id, self.numbering_prefix)
        self.sales_office = 'SLS-000'
        ErpObject.write_object_to_csv(self)
