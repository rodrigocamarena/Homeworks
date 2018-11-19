print("Welcome to the universal pocket calculator.")
print("1. Type <+> if you want to compute a sum."
      "\n2. Type <-> if you want to compute a rest."
      "\n3. Type <*> if you want to compute a multiplication."
      "\n4. Type </> if you want to compute a division."
      "\n5. Type <quit> if you want to exit.")
while True:
    prompt = 'Introduce your answer: '
    answer = input(prompt)

    if answer == "+":
        while True:
            try:
                    num = input('Introduce the first number: ')
                    num2 = input('Introduce the second number: ')
                    num = float(num)
                    num2 = float(num2)
            except ValueError:
                print("opps, please give me a proper number!")
            except:
                print("opps, something unknown occured.")
            else:
                result = num + num2
                print("The result of: ",num,"+",num2," is: ",result)
                break
    elif answer == "-":
        while True:
            try:
                    num = input('Introduce the first number: ')
                    num2 = input('Introduce the second number: ')
                    num = float(num)
                    num2 = float(num2)
            except ValueError:
                print("opps, please give me a proper number!")
            except:
                print("opps, something unknown occured.")
            else:
                result = num - num2
                print("The result of: ",num,"-",num2," is: ",result)
                break
    elif answer == "*":
        while True:
            try:
                    num = input('Introduce the first number: ')
                    num2 = input('Introduce the second number: ')
                    num = float(num)
                    num2 = float(num2)
            except ValueError:
                print("opps, please give me a proper number!")
            except:
                print("opps, something unknown occured.")
            else:
                result = num * num2
                print("The result of: ",num,"*",num2," is: ",result)
                break
    elif answer == "/":
        while True:
            try:
                    num = input('Introduce the first number: ')
                    num2 = input('Introduce the second number: ')
                    num = float(num)
                    num2 = float(num2)
            except ValueError:
                print("opps, please give me a proper number!")
            except:
                print("opps, something unknown occured.")
            else:
                result = num / num2
                print("The result of: ", num, "/", num2, " is: ", result)
                break
    elif answer == "quit":
        print("Was a pleasure working with you. See you soon!")
        break
    else:
        print("opps, invalid answer. Try again please!")


