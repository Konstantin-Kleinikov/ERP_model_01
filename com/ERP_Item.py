"""Module for handling of items"""
from dataclasses import dataclass, field, InitVar

from com.ERP_Business_Partner import Supplier
from com.ERP_Object import ErpObject


@dataclass
class Item(ErpObject):
    numbering_prefix = 'ITM'

    id: str = field(init=False)
    name: str
    supplier: Supplier
    price: float = 0
    unit_of_measure: str = 'pcs'
    weight: float = 0
    length: float = 0
    height: float = 0
    width: float = 0
    calc_volume: InitVar[bool] = False
    volume: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_volume):
        self.id = ErpObject.generate_new_seq_number(Item.numbering_prefix)
        if calc_volume:
            self.volume = (self.height * self.width * self.length)
