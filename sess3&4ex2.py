print("Welcome to the round up division exe.")
print("Before we start, if you want to exit the program type <quit> if not follow the normal process.")

while True:
    try:
        num = input('Introduce the numerator (integer>0) of the division: ')
        if num == "quit":
            print("Was a pleasure working with you. See you next time!")
            break
        num2 = input('Introduce the denominator (integer>0) of the division: ')
        if num2 == "quit":
            print("Was a pleasure working with you. See you next time!")
            break
        num = int(num)
        num2 = int(num2)
        result = (num//num2)+1

    except ValueError:
        print("opps, please give me a proper integer!")
    except ZeroDivisionError:
        print("opps, give me a denominator different to zero!")
    except:
        print("opps, something unknown occured.")
    else:
        print("The result of the round up division of ",num,"/",num2," is: ",result)