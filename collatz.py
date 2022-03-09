# collatz.py
# 
# This program asks the user to input any positive integer and outputs the successive 
# values of the following calculation:
# At each step it calculates the next value by taking the current value. If the value
# is even, divide it by two, if it is odd, multiply it by three and add one.
# The program ends when the current value is one.
#
# Author: Elaine Tynan

# There is no error checking, assuming a valid number is entered.
def collatz():
    num = int(input("Please enter a whole positive number: "))
    print(num, end = ' ')

    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        print (num, end = ' ')

# This function also gives the number of steps   
def collatz2():
    num = int(input("Please enter a whole positive number: "))
    print(num, end = ' ')

    count = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        
        count += 1
        print (num, end = ' ')
    print("\nThe number of steps is: {} ({} numbers)".format(count, (count+1)))

collatz()