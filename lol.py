
def numbers(amount=str):
    num1 = 0
    num2 = 1
    for i in range(amount):
        nums = num1 + num2
        num1 = num2
        num2 = nums
        print(nums)

amount = int(input("Amount? "))
numbers(amount)