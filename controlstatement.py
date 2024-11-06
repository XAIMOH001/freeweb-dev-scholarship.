from variables import number

temperature = 45

if temperature > 25:
    print("its too hot")
else:
    print("it's too cold")


#a program that takes num and returns the smallest
num1 = 30
num2 = 67
num3 = 56

if num1 < num2 and num1 < num3:
    print(num1, "is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number")
else:
    print(num3, "is the smallest number")


#program to check whether a number is odd or even
number = 67


if number % 2 == 0:
    print("even")
else:
    print("odd")
