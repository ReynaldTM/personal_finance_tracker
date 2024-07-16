# only pip install, not pip3.  pip3 is for Mac and linux
# for main flow of program


import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "finance_data.csv"  # class variable

    @classmethod # will have access to class itself, but not its instance
    # meaning it has access to other class methods and class variables
    def initialize_csv(cls):
        try: # "pd" are pandas
            pd.read_csv(cls.CSV_FILE) # trying to find an existing CSV file
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "category", "description"]) # making the csv file with columns
            df.to_csv(cls.CSV_FILE, index=False) # saving a local file with the class variable name above

CSV.initialize_csv()







