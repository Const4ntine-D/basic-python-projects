# Project_1: basic-calculator


def menu_display():
    print("====================")
    print("--Basic Calculator--")
    print("A: Addition")
    print("B: Subtraction")
    print("C: Multiplication")
    print("D: Division")
    print("E: Exit")


valid_values = {"A", "B", "C", "D", "E", "a", "b", "c", "d", "e"} # valid input values


while True:
    while True:
        menu_display()
        menu_choise = input("--Choose operation:")
        if menu_choise == "E" or menu_choise == "e":
            print("--End of the program--")
            quit()
        if menu_choise in valid_values:
            break
        else:
            print("There is no such operation. Try again!")
            continue
    while True:
        try:
            first_num = float(input("--Input first num: "))
            break
        except ValueError:
            print("First num is not a number. Try again!")
    while True:
        try:
            second_num = float(input("--Input second num:"))
            break
        except ValueError:
            print(f"Second num is not a number. Try again!")
            
    print("====================")
    if menu_choise == "A" or menu_choise == "a":
        result_output = first_num + second_num
        print(f"Result >>> {first_num} + {second_num} = {result_output}")
    elif menu_choise == "B" or menu_choise == "b":
         result_output = first_num - second_num
         print(f"Result >>> {first_num} - {second_num} = {result_output}")
    elif menu_choise == "C" or menu_choise == "c":
        result_output = first_num * second_num
        print(f"Result >>> {first_num} * {second_num} = {result_output}")
    elif menu_choise == "D" or menu_choise == "d":
        result_output = first_num / second_num
        print(f"Result >>> {first_num} / {second_num} = {result_output}")
    elif menu_choise == "E" or menu_choise == "e":
        print("--End of the program--")
        quit()
