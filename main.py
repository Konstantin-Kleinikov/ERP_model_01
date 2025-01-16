"""Main program script"""
from com.erp_business_partner import Customer, Supplier
from com.erp_object import ErpObject
from sls.erp_sales_order import SalesOrder
from com.erp_item import Item, ItemBOM


def main():
    ErpObject.load_data_from_csv('last_used_numbers.csv')
    # Create business partners.
    customer_1 = Customer('Fish Cans Producer "', 9729219091)
    customer_2 = Customer('Transylvania & Co"', 9729219092)
    supplier_1 = Supplier('Heavy Mechanics & Technology"', 9729219093, 14)
    supplier_2 = Supplier('Sinaps Corporation', 9729219094, 6)
    # Create Items and BOMs
    item_1 = Item('Engine Block FT 0921', supplier_1, 123.56, 'pcs', 120.00, 1.2, 0.7, 1.1, True)
    item_2 = Item('Engine Part 001', supplier_2, 60.0, 'pcs', 40.60, 0, 0, 0, False)
    item_3 = Item('Metal bolt DF64', supplier_2, 10.0, 'pcs', 0, 0, 0, 0, False)
    print(item_1)
    print(item_2)
    bom_item_1 = ItemBOM(item_1)
    bom_item_1.add_child(item_2)
    bom_item_1.add_child(item_3)
    print(f'Printing of BOM for main item: {bom_item_1.main_item.id}')
    for sub_item in bom_item_1:  # using iterator of class ItemBOM
        print(sub_item)

    # Create sales order
    sales_order_1 = SalesOrder(101,
                               customer_1,
                               '10-01-2025',
                               'EUR',
                               1000
                               )
    print(sales_order_1)
    print('-' * 60)
    count = 0
    for key, value in sales_order_1.__dict__.items():
        count += 1
        print(f'Field {count}: {key} ({value}).')

    # Copy existing sales order to a new sales order
    sales_order_2 = sales_order_1.copy_sales_order()
    sales_order_2.customer = customer_2
    print(sales_order_2)


if __name__ == '__main__':
    main()
