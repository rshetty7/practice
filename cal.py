def add (x,y):
    return x + y

def subtract (x,y):
    return x - y

def division (x,y):
    return x / y

def multiply (x,y):
    return x * y




print("select operation\n 1.addition\n 2.subtract\n 3.division\n 4.multiply")


while True:
    choice = input("enter your choice (1/2/3/4) :")
    if choice in ('1','2','3','4'):
        num1 =int(input("enter the first number:"))
        num2 = int(input("enter a secound number:"))
        if choice == '1':
            print(add(num1,num2))
        if choice == '2':
            print(subtract(num1,num2))
        if choice == '3':
            print(division(num1,num2))
        if choice == '4':
            print(multiply(num1,num2))
            break
    else :
        print("invalid input")
            