import csv
import os
import pandas as pd


class FileManager:
    def __init__(self, file_path, fieldnames):
        self.file_path = file_path
        self.fieldnames = fieldnames

    def check_file(self):
        if not os.path.exists(
                self.file_path) or os.path.getsize(
                self.file_path) == 0:
            self.create_file()

    def create_file(self):
        with open(self.file_path, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()

    def validate_file(self):
        with open(self.file_path, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            existing_fieldnames = next(reader, None)

        if existing_fieldnames != self.fieldnames:
            self.create_file()

    def read_file(self):
        return pd.read_csv(self.file_path)

    def write_file(self, df):
        df.to_csv(self.file_path, index=False)
