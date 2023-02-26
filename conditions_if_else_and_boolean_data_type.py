calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(number_of_days):
    # condition_check = number_of_days > 0
    # print(type(condition_check))
    # if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}"
    # elif number_of_days == 0:
    #     return "you entered a 0, please enter a valid positive number"
    # else:
    #     return "you entered a negative value, so no conversion for you!"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
    else:
        print("your input is not a valid number. Don't ruin my program!")


user_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
validate_and_execute()



# print(type("this should be a string type")) #string
# print(type(30.99))  # float