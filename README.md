# ERP_model_01
This simple ERP-model allows to create and handle business-partners, items, sales orders and financial documents
using different patterns and techniques in Object-Oriented Programming.

The main.py module runs the creation of objects

## The Project Structure

### Master Data (com)
The most common super-class [ErpObject|com/ERP_Object.py] is used:
* to handle a csv-file read/write activities for any chaild object
* to generate a new sequence number for any object within the numbering prefix
* to set generic attributes for child any object

Base module com/*ERP_Master_Data.py* allows is used for:
* getting the currency rate that is effective at document date of an object.

### Sales (sls)
...

### Purchases (pur)
...
