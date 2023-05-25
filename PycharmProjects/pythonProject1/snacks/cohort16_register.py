def cohort16_register():
    list_of_student_names_available = {
        'shola': 24,
        'tolu': 34,
        'bola': 26,
        'folake': 27,
    }
    new_name = input("Enter your name: ")
    new_name = new_name.lower()
    for names in list_of_student_names_available.keys():
        if names != new_name:
            age = int(input(f"Hi {new_name} kindly input your age: "))
            list_of_student_names_available[new_name] = age
            for key in list_of_student_names_available.keys():
                if new_name == key:
                    return f"Your name is {key} and your age is {list_of_student_names_available[new_name]}"
        else:
            # if new_name == names:
            return f"Hi {new_name} Your age is {list_of_student_names_available[new_name]}"

    ## 0R


def cohort16_register2():
    names_age = {"tolu": 23, "jide": 45, "bola": 34, "afolabi": 20}

    name = input("Enter your name: ").lower()

    if name in names_age:
        age = names_age[name]
        return f"Hi, {name}, you are {age} years old."
    else:
        age = int(input("Your name is not in the dictionary. Please enter your age: "))
        names_age[name] = age
        return f"Hi, {name}, you are {age} years old (added to the dictionary)"


result = cohort16_register()
print(result)
# cohort16_register2()
cohort16_register()
