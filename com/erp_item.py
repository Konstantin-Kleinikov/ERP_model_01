"""Module for handling of items"""
from dataclasses import dataclass, field, InitVar

from com.erp_business_partner import Supplier
from com.erp_object import ErpObject


@dataclass
class Item(ErpObject):
    """Class for handling items (purchased or produced)"""
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


class ItemBOM(ErpObject):
    """Class for composing Item's Bill of Material"""
    def __init__(self, main_item: Item):
        self.main_item = main_item
        self._sub_items = []

    def __repr__(self):
        return 'ItemBom({!r})'.format(self.main_item)

    def add_child(self, sub_item: Item):
        self._sub_items.append(sub_item)

    def __iter__(self):
        """Iterator for output of subitems"""
        return iter(self._sub_items)