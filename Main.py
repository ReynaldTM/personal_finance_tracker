# only pip install, not pip3.  pip3 is for Mac and linux
# for main flow of program

import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description


class CSV:
    CSV_FILE = "finance_data.csv"  # class variable
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

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

    @classmethod
    def get_transaction(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        # making a dataframe
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        # df[at value] is accessing all values in date column using pandas, converting into format stated
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = ((df["date"] >= start_date) & (df["date"]) <= end_date)
        # checking if data in current row on column date is less than or equal to end date, applies to every row
        # "&" only used when working with pandas or Mask specifically
        filtered_df = df.loc[mask]
        # locating different rows that mask matches then return filtered dataframe

        if filtered_df.empty:
            print("No transactions found in given date range")
        else:
            print(f"Transaction from {start_date.stftime(CSV.FORMAT)} to {end_date.stftime(CSV.FORMAT)}"
                  )
            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}
                                        )
                  )
            # key & pair, date is key. Function is pair using lambda as pair is calling all entry in date column

            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary: ")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income-total_expense):.2f}")


def add():
    CSV.initialize_csv()
    date = get_date("Please enter date of transaction  (dd-mm-yyyy format),  or enter for today's date: ",
                    allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


add()
