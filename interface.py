'''
File Name: interface.py
Dependencies: calc.py
Purpose: Contains code that operates the interface of the calculator app
(i.e mostly printing, running certain commands)
'''
# import statements
import calc
import sys
# Write your code here:

# to update the dictionary to a file "TraderLatinas"


def save(dictionary):
    f = open("TraderLatinas.txt", "a")  # opens file for appending to it
    # for x in dictionary:
    #     f.write("{" + x + ": " + dictionary[x]+"}")
    f.write(str(dictionary) + ", ")  # writes dictionary as a string to file
    f.close()  # closes it for posterior use

# main function. recursive


def loop(dictionary):
    user_input = input("What's your fav stock? ")  # input from user
    # goes into calc, function that returns the alpha
    alpha = calc.calc(user_input)
    if "$" in user_input.strip():  # escape
        sys.exit()
    elif user_input.lower().strip() == "help":  # help
        print("\033[1;31;41m There are 3 commands that you can use: Buy, Sell, and $. Buy: You buy a stock, we tell you if its a good decision. Sell: You sell a stock, we tell you if its a good decision. $: Exit the trading calculator")
        print("\033[0m")
        loop(dictionary)

    else:
        # another info from user, our two operations
        option = input("Do you want to buy or sell? ")
        if user_input not in dictionary:

            if (alpha > 0) and (option.lower().strip() == "buy"):

                print("Alpha: " + str(alpha) + "%. ")

                dictionary[user_input] = {
                    "Buy": "Don't buy. Alpha is high, it wouldn't be wise to buy it now. Wait a little.", "Sell": "Sell! Alpha is super nice. Go for it. You'll make money.", "Alpha": alpha}

                print(dictionary[user_input]
                      [option.lower().strip().capitalize()])
                save(dictionary)
                loop(dictionary)

            elif (alpha > 0) and (option.lower().strip() == "sell"):

                dictionary[user_input] = {
                    "Buy": "Don't buy. Alpha is high, it wouldn't be wise to buy it now. Wait a little.", "Sell": "Sell! Alpha is super nice. Go for it. You'll make money.", "Alpha": alpha}

                print(dictionary[user_input]
                      [option.lower().strip().capitalize()])

                print("Alpha: " + str(alpha) + "%. ")
                save(dictionary)
                loop(dictionary)
            elif (alpha <= 0) and (option.lower().strip() == "sell"):

                dictionary[user_input] = {
                    "Buy": "Buy! You might make a lot of profit after this.", "Sell": "Don't Sell! You won't make as much profit if you do it now.", "Alpha": alpha}
                print(dictionary[user_input]
                      [option.lower().strip().capitalize()])

                print("Alpha: " + str(alpha) + "%. ")
                save(dictionary)
                loop(dictionary)

            elif (alpha <= 0) and (option.lower().strip() == "buy"):

                dictionary[user_input] = {
                    "Buy": "Buy! You might make a lot of profit after this.", "Sell": "Don't Sell! You won't make as much profit if you do it now.", "Alpha": alpha}
                print(dictionary[user_input]
                      [option.lower().strip().capitalize()])

                print("Alpha: " + str(alpha) + "%. ")
                save(dictionary)
                loop(dictionary)

        else:
            print(dictionary[user_input]
                  [option.lower().strip().capitalize()])
            loop(dictionary)
