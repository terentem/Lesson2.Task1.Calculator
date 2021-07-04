#Lesson 2. Task1. Calculator

value1 = input('Enter value1: ')

if not value1.isdigit():
    value1 = input("Enter numeric value1: ")

value1_id_digit = value1.isdigit()


value2 = input("Enter value2: ")
if not value2.isdigit():
    value2 = input("Enter numeric value2: ")

value2_is_digit = value2.isdigit()


if not value1_id_digit and value2_is_digit:
        print("Calculator can't use non-numeric value1")
        exit()
if value1_id_digit and not value2_is_digit:
        print("Calculator can't use non-numeric value2")
        exit()
if not value1_id_digit and  not value2_is_digit:
        print("Calculator can't use non-numeric value1 and non-numeric value2")
        exit()

action = input("Enter action + or - : ")

if action == '+' and value1_id_digit and value2_is_digit:
     result = int(value1) + int(value2)
     print("Result= ", result)
elif action == '-' and value1_id_digit and value2_is_digit:
    result = int(value1) - int(value2)
    print('Result= ', result)



