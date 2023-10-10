#input to get user supplied year to be checked
year = int(eval(input("Which year do you want to check? ")))

#logic to determine if the year entered is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap Year!')
        else:
            print('Not a leap year.')
    else:
        print('Leap Year!')
else:
    print('Not a leap year.')
