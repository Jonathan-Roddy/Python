
try:
    answer = 10 / int(input("Enter Number: "))
except ZeroDivisionError as e:
    print(e)
except:
    print("Caught any exception")       

