# ERP_model_01
This simple ERP-model allows to create and handle business-partners, items, sales orders and financial documents
using different patterns and techniques in Object-Oriented Python Programming.

The [main.py](https://github.com/Konstantin-Kleinikov/ERP_model_01/blob/master/main.py) module runs the creation and handling of objects.

## The Project Structure

### Master Data (com)
The most common super-class __ErpObject__ in [com/ERP_Object.py](https://github.com/Konstantin-Kleinikov/ERP_model_01/blob/master/com/ERP_Master_Data.py) module is used:
* to handle a csv-file read/write activities for any child object
* to generate a new sequence number for any object within the numbering prefix
* to set a generic attributes for any child object

Base module com/*ERP_Master_Data.py* is used for:
* getting the currency rate that is effective at document date of an object.

### Sales (sls)
...

### Purchases (pur)
...
