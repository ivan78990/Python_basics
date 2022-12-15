to_unit = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * to_unit} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("It's zero!")
        else:
            print("You entered a negative number")
    except ValueError:
        print("You input is not a valid number")


user_input = ""
while user_input != "exit":
    user_input = input("Conversion!\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": "hours"}

    # print(list_of_days)
    # print(set(list_of_days))
    # print(type(list_of_days))
    # print(type(set(list_of_days)))
    # for num_of_days_element in set(list_of_days):
    #     validate_and_execute()



