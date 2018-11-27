def divisors(x):
    global list
    for i in range(1, (x + 1)):
        result = x % i
        if result == 0:
            list.append(i)
            continue
    return list


list = []
token =False
num = 0

while not token:
    try:
        num = int(input("Introduce an integer: "))
        token = True
    except ValueError:
        print('Error, introduce a valid integer. \n')

if num < 0:
    num = -num
    divisors(num)
    print(list)
else:
    divisors(num)
    print(list)