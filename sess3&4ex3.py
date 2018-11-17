import math
print("Welcome to the surface computation of a cricle.")
print("Before we start, if you want to exit the program type <quit> if not follow the normal process.")

while True:
    try:
        num = input('Introduce the radius of the circle: ')
        if num == "quit":
            print("Was a pleasure working with you. See you next time!")
            break
        num = float(num)
        result = math.pi*pow(num, 2)

    except ValueError:
        print("opps, please give me a proper number!")
    except:
        print("opps, something unknown occured.")
    else:
        print("The surface of this circle is: ",result)