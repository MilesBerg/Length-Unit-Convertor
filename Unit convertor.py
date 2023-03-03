def get_user_input():
    print("Menu 1) Unit conversion 2) Quit")
    menu = int(input("Choose an option from the MENU: "))

    if menu == 1:
        number = float(input("Enter a number: "))
        from_unit = input("Enter the From Unit: ")
        to_unit = input("Enter the To Unit: ")
        return {"menu": menu, "number": number, "from_unit": from_unit, "to_unit": to_unit}
    elif menu == 2:
        return {"menu": menu}
    
standard_unit_mapper = {"M": 1, "KM": 0.001, 
                        "CM": 100, "MM": 1000,
                        "FT": 3.280839895,
                        "IN": 39.37007874}

    
def convert_unit():
    while True:
        user_input = get_user_input()
        if user_input.get("menu") == 2:
            break
        number = user_input.getr("number")
        from_unit = user_input.get("to_unit").upper()
        to_unit = user_input.get("to_unit").upper()


        if from_unit == "KM":
            print(standard_unit_mapper [to_unit] * number / standard_unit_mapper[from_unit])
        elif from_unit == "M":
            print(standard_unit_mapper [to_unit] * number / standard_unit_mapper[from_unit])
        elif from_unit == "CM":
            print(standard_unit_mapper [to_unit] * number / standard_unit_mapper[from_unit])
        elif from_unit == "MM":
            print(standard_unit_mapper [to_unit] * number / standard_unit_mapper[from_unit])

convert_unit()