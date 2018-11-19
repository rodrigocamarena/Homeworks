print("\n¡Welcome!\n\n"
      "\nYou are trapped in a magic maze. Every decision will determine your destiny."
      "\nBe patient but even more wiser with your decisions."
      "\n\nRead the following instructions carefully: "
      "\n   First of all, it is important to understand, that you will only escape from this magic maze"
      "\n   if you find the secret combination compound of a sequence of 6 direction movements."
      "\n   There are 4 different type of direction movements: [N, S, W, E]."
      "\n   Secondly, If the escape chain is broken, you will start from the beginning. "
      "\n   Suppose you commit a mistake during the sequence."
      "\n   This breaks the chain an we must start again from the first valid move."
      "\n   Last but no least, you only have 3 lives, and you will loose 1 live after 10 moves."
      "\n\nGood luck traveler! "
      "\n\n\n           List of valid tokens"
      "\n1. N [North]."
      "\n2. S [South]."
      "\n3. W [West]."
      "\n4. E [East]."
      "\n5. R [Restart]."
      "\n6. I [Display intrusctions."
      "\n7. L [List of tokens]."
      "\n8. D [Display status]"
      "\n9. Q [Exit as a desertor].")

number = int(1)
attempt = int(1)
counter = int(0)
lives = int(3)
secret = ["S", "S", "N", "W", "E", "S"]
quit = 0
movement = []
while True:
    if lives > 0:
        while True:
            print("\nYou are finding the ", (counter+1), "secret word.\n")
            y = input("Input: ")
            movement.append(y.upper())
            print("\n")
            if movement[counter] == "L":
                print('\n           List of valid tokens'
                      '\n1. N [North].'
                      '\n2. S [South].'
                      '\n3. W [West].'
                      '\n4. E [East].'
                      '\n5. R [Restart].'
                      '\n6. I [Display intrusctions.'
                      '\n7. L [List of tokens].'
                      '\n8. S [Display status]'
                      '\n9. Q [Exit as a desertor].')
                continue
            elif movement[counter] == "I":
                print("\n¡Welcome!\n\n"
                      "\nYou are trapped in a magic maze. Every decision will determine your destiny."
                      "\nBe patient but even more wiser with your decisions."
                      "\n\nRead the following instructions carefully: "
                      "\n   First of all, it is important to understand, that you will only escape from this magic maze"
                      "\n   if you find the secret combination compound of a sequence of 6 direction movements."
                      "\n   There are 4 different type of direction movements: [N, S, W, E]."
                      "\n   Secondly, If the escape chain is broken, you will start from the beginning. "
                      "\n   Suppose you commit a mistake during the sequence."
                      "\n   This breaks the chain an we must start again from the first valid move."
                      "\n   Last but no least, you only have 3 lives, and you will loose 1 live after 10 moves."
                      "\n\nGood luck traveler! ")
                continue
            elif movement[counter] == "R":
                lives = 3
                number = 1
                attempt = 1
                counter = 1
                continue
            elif movement[counter] == "S" or movement[counter] == "W" or movement[counter] == "E" or movement[counter] == "N":
                if number > 10:
                    print("We are so sorry, but you have lost a life. :(.")
                    lives = lives - 1
                    number = 1
                    print("\nBut don´t worry you still have: ", lives)
                    continue
                if movement[counter] == secret[counter]:
                    if counter == 5:
                        print("Congrats! You successfully scaped from the magic maze!")
                        print("Rest of lives: ", lives)
                        print("Number of movements: ", attempt)
                        quit = 1
                        break
                    print("¡Well done! Keep working.\n")
                    print("Number of lives: ", lives, "\nResting of movements in this life: ", (10 - number),
                          "\nNumber of attempts in this live: ",
                          attempt)
                    number = number + 1
                    counter = counter + 1
                    attempt = attempt + 1
                    continue
                elif movement[counter] != "S" or movement[counter] == "W" or movement[counter] == "E" or movement[
                    counter] == "N":
                    print("¡Bad luck! try again.\n")
                    print("You are starting from the very first secret letter")
                    print("Number of lives: ", lives, "\nResting of movements in this life: ", (10 - number),
                          "\nNumber of attempts in this live: ",
                          attempt)
                    attempt = attempt + 1
                    number = number + 1
                    counter = 0
                    movement[:] = []
                    continue

            elif movement[counter] == "D":
                print("         Displaying your status")
                print("Number of lives: ", lives)
                print("Number of movements: ", counter)
                continue

            elif movement[counter] == "Q" or "q":
                quit = 1
                break
            else:
                print("opps, invalid movement. Try again.")
                continue
    else:
        print("Game Over.")
        print("Restarting the game...")
        lives = 3
        number = 0
        attempt = 0
        continue

    if quit == 1:
        break
