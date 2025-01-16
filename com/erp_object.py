"""Module for the most generic ERP-object class"""
import csv, os


PROJECT_PATH = os.getcwd() + os.sep  # use the 'get current working directory' function
last_used_numbers: dict[str, int] = dict()

class ErpObject:

    def __init__(self, numbering_prefix=None):
        self.erp_version = 'LN 10.8 084'
        self.erp_object_type = type(self).__name__
        if numbering_prefix:
            self.id = ErpObject.generate_new_seq_number(numbering_prefix)



    @classmethod
    def check_csv_file_exists(cls, csv_file) -> bool:
        """
        Checks whether the CSV-file exists for ERP object or not.

        If file exists then the check is done on whether it is empty or not.

        :param csv_file: CSV-file name
        :return: True or False
        """
        search_file = PROJECT_PATH + csv_file
        return True if os.path.exists(search_file) else False


    @classmethod
    def load_data_from_csv(cls, csv_file):
        if ErpObject.check_csv_file_exists(csv_file):
            with open(csv_file) as csvfile:
                reader = csv.DictReader(csvfile, delimiter='~')
                fieldnames = list(reader.fieldnames)
                for row in reader:
                    last_used_numbers[row[fieldnames[0]]] = int(row[fieldnames[1]])
        print(last_used_numbers)
        return last_used_numbers


    def write_object_to_csv(self) -> None:
        """
        Writes ERP object to dedicated CSV-file.

        :param self: ERP object
        :return: new CSV-file with record or new record in existing CSV-file
        """
        csv_file = type(self).__name__.lower() + 's' + '.csv'
        input_data = self.__dict__
        field_names = [key for key in input_data.keys()]

        if ErpObject.check_csv_file_exists(csv_file):
            with open(csv_file, 'a', newline='') as csvfile:  # encoding='utf-8',
                writer = csv.DictWriter(csvfile, fieldnames=field_names, delimiter='~', dialect='excel')
                writer.writerow(input_data)
        else:
            with open(csv_file, 'w', newline='') as csvfile:  # encoding='utf-8',
                writer = csv.DictWriter(csvfile, fieldnames=field_names, delimiter='~', dialect='excel')
                writer.writeheader()
                writer.writerow(input_data)

    @staticmethod
    def generate_new_seq_number(numbering_prefix):
        """
        Generate new sequence number for specified ERP object type.

        If object type is not specified then default numbering prefix is used.

        :return: str, new sequence number for object type prefix
        """

        try:
            last_number = last_used_numbers[numbering_prefix]
        except IndexError:
            # Last used sequence number not found for prefix and object_type
            return None
        else:
            last_number += 1
            last_used_numbers[numbering_prefix] = last_number
            return f'{numbering_prefix} - {last_number}'