def addition(number1, number2):
    print(int(number1) + int(number2))
def subtraction(number1, number2):
    print(int(number1) - int(number2))
def multiplication(number1, number2):
    print(int(number1) * int(number2))
def division(number1, number2):
    print(int(number1) / int(number2))
def increment(number1):
    print(int(number1) + 1)
def decrement(number1):
    print(int(number1) - 1)

select = int(input("Select math 1-6: "))
num1 = int(input("number1 "))
num2 = int(input("number2 "))

if select == 1:
    addition(int(num1), int(num2))
if select == 2:
    subtraction(int(num1), int(num2))
if select == 3:
    multiplication(int(num1), int(num2))
if select == 4:
    division(int(num1), int(num2))
if select == 5:
    increment(int(num1))
if select == 6:
    decrement(int(num1))
