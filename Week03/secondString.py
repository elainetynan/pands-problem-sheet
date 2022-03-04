# secondString.py
# 
# This program asks a user to input a string and outputs every second letter 
# in reverse order.
#
# Author: Elaine Tynan

text = input("Please enter a sentence: ")
reverse = text[::-1]

finalText = ""
for i in range(len(reverse)):
    if i%2 == 0:
        finalText = finalText + reverse[i]

print(finalText)