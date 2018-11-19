from random import randint


def random():
    global x
    for i in range(10):
        x = int(0)
        x = x + randint(1,1000)

    return x


print("\n ¡Welcome to the Random Machinery Sum¡")
prompt = ""
while not prompt.lower() == 'quit':
    print("\n1. Type <Random> to make the machine work")
    print("2. Type <Quit> if you want to exit.")
    prompt = input('Input: ')

    if prompt.lower() == "random":
        random()
        print("Your random number is: ", x)
        continue
    elif prompt.lower() == "quit":
        print("\n¡See you soon!")
    else:
        print('¡invalid token. \nPlease try again.')
