# for data from user will contain:
# input statements
# validating data


from datetime import datetime

def get_date(prompt, allow_default=False):# prompt is input is question before date come
                                                                   # for getting date in multiple different places
                                                                   # allow_default = will select current date by hitting return.
                                                                   # since its set to False, date will be required
    date_str = input(prompt)
    if allow_default and not date_str: # allow_default is True and date_str is None
        return datetime.today().strftime("%d-%m-%Y") # return current date at format, date, month, year
    try:
        valid_date = datetime.strftime(date_str,"%d-%m-%Y")
        return valid_date.strftime(date_str,"%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please enter date in dd-mm-yyyy format")
        return get_date(prompt, allow_default=False)

def get_amount():
    pass

def get_category():
    pass

def get_description():
    pass