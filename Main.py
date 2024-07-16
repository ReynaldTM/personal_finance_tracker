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
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])



