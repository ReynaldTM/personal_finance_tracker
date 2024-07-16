# only pip install, not pip3.  pip3 is for Mac and linux
# for main flow of program


import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = "finance_data.csv"  # class variable
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod  # will have access to class itself, but not its instance
    # meaning it has access to other class methods and class variables
    def initialize_csv(cls):
        try:  # "pd" are pandas
            pd.read_csv(cls.CSV_FILE)  # trying to find an existing CSV file
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)  # making the csv file with columns
            df.to_csv(cls.CSV_FILE, index=False)  # saving a local file with the class variable name above

    @classmethod
    def add_entry(cls, date, amount, category, description):  # new class method taking new data
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }  # new data created as a dictionary
        with open(cls.CSV_FILE, "a", newline="") as csvfile:  # context manager,
            # automatically handles file closing, memory leaks, etc.
            # opened CSV file in append mode
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)  # writing diction into CSV file
            writer.writerow(new_entry)  # new data being written into their own rows according to columns
            print("Entry added successfully")


CSV.initialize_csv()
CSV.add_entry("20-07-24", 125.65, "Income", "salary")
