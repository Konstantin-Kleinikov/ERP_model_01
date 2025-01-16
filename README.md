# ERP_model_01
This simple ERP-model allows to create and handle business-partners, items, sales orders and financial documents
using different patterns and techniques in Object-Oriented Python Programming.

The [main.py](https://github.com/Konstantin-Kleinikov/ERP_model_01/blob/master/main.py) module runs the creation and handling of objects.

## The Project Structure

### Master Data (com)
The most common super-class __ErpObject__ in [erp_object.py](https://github.com/Konstantin-Kleinikov/ERP_model_01/blob/master/com/erp_master_data.py) module is used:
* to handle a csv-file read/write activities for any child object
* to generate a new sequence number for any object within the numbering prefix
* to set a generic attributes for any child object

Module [erp_master_data.py](https://github.com/Konstantin-Kleinikov/ERP_model_01/blob/master/com/erp_master_data.py) is used for:
* getting the currency rate that is effective at the document date of an object.

Module [erp_document.py](https://github.com/Konstantin-Kleinikov/ERP_model_01/blob/master/com/erp_document.py) is used for:
* definition of base class Document for all ERP documents:
  * sales orders, purchase_orders, invoices, journal entries, etc
* static method for calculating amount in local currency using the rate, effective at document date 

Module [erp_business_partner.py](https://github.com/Konstantin-Kleinikov/ERP_model_01/blob/master/com/erp_business_partner.py) is used for:
* definition of base class BusinessPartner and child classes: Customer and Supplier

Module [erp_item.py](https://github.com/Konstantin-Kleinikov/ERP_model_01/blob/master/com/erp_item.py) is used for:
* definition of Item and ItemBOM classes via @dataclass decorator:
  * Class Item defines attributed and method for items (goods) that are purchased
    * from suppliers or produced at company's job shop
  * Class ItemBOM defines the Bill-of-Material structure: main item and sub-items that is
    * used in company's job shop

### Sales (sls)
Module [erp_sales_order.py](https://github.com/Konstantin-Kleinikov/ERP_model_01/blob/master/sls/erp_sales_order.py) is used for:
* definition of SalesOrder class
* method for copying existing sales order to a new sales order

### Purchases (pur)
...

### Interim files
CSV-files are used to temporary store the data of created ERP objects. 
