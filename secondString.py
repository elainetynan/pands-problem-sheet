# secondString.py
# 
# This program asks a user to input a string and outputs every second letter 
# in reverse order.
#
# Author: Elaine Tynan
#
# Updated: 09/03/2022
# By: Elaine Tynan
# Changes after feedback from Andrew
# I have left the original code so that I can go back and review it.
# The suggested way by Andrew appears to be far more efficient.

text = input("Please enter a sentence: ")
finalText = text[::-2] # This is a much more efficient way.

#reverse = text[::-1]
#finalText = ""
#for i in range(len(reverse)):
#    if i%2 == 0:
#        finalText = finalText + reverse[i]

print(finalText)