calculation_to_units = 24  # global variable
name_of_unit = "hours" # global variable

def days_to_units(number_of_days, custom_message):  # local variable
    print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message, "All good")


def scope_check(number_of_days):
    my_var = "variable inside function"
    print(name_of_unit)
    print(number_of_days)
    print(my_var)

scope_check(2)

