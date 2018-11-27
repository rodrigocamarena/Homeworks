import math


def power(a, b):
    global result
    result = math.pow(a, b)
    return result

result = 0
token = False
while not token:
    try:
        a = float(input('Introduce a number: '))
        b = float(input('Introduce the second number: '))
        token = True
    except:
        print('Error, given value not valid.\n')

power(a, b)
print('The result of ', a, ' to the power of ', b,' is: ', result)