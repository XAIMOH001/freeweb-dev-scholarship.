try:
    print(number)
except:
    print("an error occurred")


num1 = 39
num2 = 0
try:
    print(num1 / num2)

except:
    print("a ZeroDivisionError occurred")
finally:
    print("Success")