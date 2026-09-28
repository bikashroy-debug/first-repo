# def addition():
#     return int(input("Enter num1: "))+int(input("Enter num2: "))
# print(addition())
def square():
    try:
        num=int(input("Enter a number "))

    except ValueError:
        print("That is not a valid number ")

    return num*num
print (square())