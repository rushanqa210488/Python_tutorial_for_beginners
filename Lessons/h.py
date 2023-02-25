calculation_to_units = 24
name_of_unit = "hours"

# Functions
def days_to_units(number_of_days, custom_message):
    print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message, "All good")

days_to_units(35, "awesome")
days_to_units(365, "in one year")

def days_to_unit(days, hours, minutes, custom_message):
    print(f"{days} days are {days * hours * minutes} minutes")
    print(custom_message)


days_to_unit(20, 24, 60, "Looks good!")
days_to_unit(3, 24, 60, "Super!")
