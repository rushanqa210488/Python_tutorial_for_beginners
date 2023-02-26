calculation_to_units = 24
name_of_unit = "hours"

# input
def days_to_units(number_of_days):  # local variable
    return(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}")

user_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input)
print(calculated_value)
# Functions wiht Return Values



