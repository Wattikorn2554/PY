letter = input()
number = input()


if letter == 'H' and number == '4567':
        print("safe unlocked")
elif letter =='H':
     print("safe locked - change-digit")
elif number =='4567':  
    print("safe locked - change-char")
elif letter != 'H' and number != '4567':
    print("safe locked")