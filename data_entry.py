# for data from user will contain:
# input statements
# validating data


from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense", "G": "Grocery", "L": "Luxury Expenses", "H": "Health Care"}


def get_date(prompt, allow_default=False):  # prompt is input is question before date come
    # for getting date in multiple different places
    # allow_default = will select current date by hitting return.
    # since it's set to False, getting current date won't allow an empty input, until valid input is entered

    date_str = input(prompt)
    if allow_default and not date_str:
        # allow_default is True and date_str is None
        return datetime.today().strftime(date_format)
        # return current date at format, date, month, year

    try:
        valid_date = datetime.strptime(date_str, date_format)
        # takes date_str and converts into datetime object that is valid
        return valid_date.strftime(date_format)
        # converts it back into string representation that is in format

    except ValueError:
        print("Invalid date format. Please enter date in dd-mm-yyyy format")
        return get_date(prompt, allow_default=False)
        # recursive function


def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        # a float is whole with decimal number
        if amount <= 0:
            raise ValueError("Amount must be a non-negative, non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input(
        "Enter the category: \n'I' for Income \n'E' for Expense \n'G' for Grocery,"
        "\n'L' for Luxury Expenses \n'H' for Health Care\n"
    ).upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category.  Please enter n'I' for Income \n'E' for Expense \n'G' for Grocery,"
        "\n'L' for Luxury Expenses \n'H' for Health Care\n")
    return get_category()


def get_description():
    return input("Enter a description (Optional): ")
