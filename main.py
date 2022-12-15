

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("It's zero!")
        else:
            print("You entered a negative number")
    except ValueError:
        print("You input is not a valid number")


user_input_message = "Conversion!\n"







# my_list = ["20", "30"]
# print(my_list[1])
#
# my_dictionary = {"days": 20, "unit": "hours", "message": "all good" }
# print(my_dictionary["days"])
# print(my_dictionary["unit"])
# print(my_dictionary["message"])

    # print(list_of_days)
    # print(set(list_of_days))
    # print(type(list_of_days))
    # print(type(set(list_of_days)))
    # for num_of_days_element in set(list_of_days):
    #     validate_and_execute()



