import csv
import os
import pandas as pd

class FileManager:
    def __init__(self, file_path, fieldnames):
        self.file_path = file_path  # path to the csv file
        self.fieldnames = fieldnames  # field names for the csv file

    # check if the file exists or is empty, otherwise create it
    def check_file(self):
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            self.create_file()  # create a new file if missing or empty

    # create the csv file with headers
    def create_file(self):
        with open(self.file_path, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()  # write the headers to the file

    # validate the file has correct headers
    def validate_file(self):
        with open(self.file_path, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            existing_fieldnames = next(reader, None)  # get current headers

        if existing_fieldnames != self.fieldnames:
            self.create_file()  # recreate the file if headers dont match

    # read the csv file and return as a pandas dataframe
    def read_file(self):
        return pd.read_csv(self.file_path)

    # write the dataframe to the csv file
    def write_file(self, df):
        df.to_csv(self.file_path, index=False)
