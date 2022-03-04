# pands-problem-sheet
Weekly problem sheets

I was sick with covid the last 2 weeks (Weeks 5 & 6) I'm not sure if the instructions for the problem sheet went up before that, if so I don't know how I missed them. If it was in week 5 or 6, I did do the work but having gone back over it, I realise my head really wasn't right at the time.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Week 02
Having come from a java backgroud I am finding I am making simple syntax errors such as putting in semi-colons and using brackets in loops, if-statements, etc.

Weekly Problem Sheet
bmi.py is a program that calculates a body mass index given a height and weight.
The input must be in centimentres and kilograms.
It firstly converts the CMs to meters, then uses the formula
    bmi = (kg/meters) to the power of 2
to calculate the bmi, which is then output to 2 decimal places.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Week 03
secondString.py asks a user to input a string and outputs every second letter in reverse order.
It uses the buit in function to reverse the string first in the line:
    reverse = text[::-1]
It then sets up an empty string.
Then it loops through the reversed stings index and if the index is an even number (i%2 == 0) it appends the corresponding character to the new string.
Finally it prints the new string.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Week 04
I found this problem very interesting and if I ever have the time I would like to do some research on this, even if it is "career suicide"

Weekly Problem Sheet
collatz2.py asks the user to input any positive integer and outputs the successive values of the following calculation:
At each step it calculates the next value by taking the current value.
If the value is even, divide it by two, if it is odd, multiply it by three and add one.
The program ends when the current value is one.

I wrote this assuming a valid number is entered.
it is actaully a simple calcuation that checks if the number is even (if num % 2 = 0), if so it divides it by 2 (I used num //= 2 to do an integer divide, although it is probably not necessary but it gave me an integer output without formatting).
If the number is not even you simply mutltiply it by 3 and add 1 (num = num * 3 + 1).
This is all carried out in a while loop that checks that the number is not equal to 1 (while num != 1:)

I also included a function that counts the number of steps it takes to reach 1 becuase they were talking about this in the YoutTube video.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Week 05
task05.py gets the data (and time) from the system and checks if it is a weekday or weekend.
I needed to import the datetime module to do this. I got the day by getting todays datetime and calling the weekday function to get the actual day of the week.
The day of the week is return as an integer between 0 & 6, therefor 0, 1, 2, 3 & 4 are week days and 5 & 6 are weekend.
This meant a simple if-statement could be use to determine if it is a weekday (if day < 5:) or not (no need to check again, because if it is not a weekday, it must be a weekend).
In the if statement, if it is a weekday, it prints:
    "Unfortunately today is a weekday"
if it is a weekend it prints:
    "It is the weekend, yay!"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Week 06
squareRoot.py takes a positive floating-point number as input and outputs
an approximation of its square root.

I did some research on the newton method. Immediate;y I found the answr invarious language. I read the java code to find out how to do the calculation and then with that knowledge wrote the python code.

Weekly problem sheet
The code asks the uiser to enter a number to get a square root of, if the user inserts 0 or less it tells them this is not a valid number for getting a square root, otherwise it calls the function to get the square root and prints the answer to the screen.
The function takes a copy of the original number (x) becuase that number is used and changed throughout the lop while doing the calculations, but it also needs the original number.
I have set a margin or error of 0.00001 becuase this is used to check each time through the loop if the value is correct within this margin of error.
The loop does the following:
    It uses the formula: sqRoot = 0.5 * (x + (num / x)) to calculate an estimated square root.
    Then it checks if this value is withing the margin of error of the value copied originally form the number input.
        If it is the square root has been calulated and it breaks out of the loop
    It the square root has not been found it sets the copied value (x) equal to the square root estimate that has just been calculated
The loop will continue util the estimated square root is within the margin of error.
Once the loop is exited the square root is returned.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Week 07
I found that I am still looking up many of the functions in python to do simple things. I went down a wormhole when working through the lab and trying to load the file into the student dict. This was becuase I forgot the the JSON file could be read in as a dict and assumed it was a string. As a result I spent a lot of time looking up string functions to split the string and build a list of dicts which had a list of a dict in it.

Weekly problem sheet
es.py reads in a text file and outputs the number of e's it contains.

This was easier and cleaner to do when broken into separate functions.

Firstly I did the function that takes a string.
Firstly it sets all the text to lowercase so that it will count all 'e's, not just lower case 'e's.
It then iterates trough the text and compares each character to the letter 'e', if it is equal it adds 1 to count, otherwise ti does nothing.
Once the loop has completed it returns the count.

The function that reads the file firstly checks if the file exists (a simple typo could cause the program to crash), if the file does not exist it returns a count of -1 (this could be used by a calling method to determine what to do if the file is invalid). The error checking could also be done with a try & except block.

If the file exists it opens the file in the mode read and text file. It then reads in the data from the text file and stores it in the variable text.
Then it returns the counts of 'e's by calling the function 'countEs' and passing the variable 'text' into it.

I have set the filename to the system argument (filename = sys.argv[1]), originally I assumed it would be the first element in the list sys.argv but that was the actual program name so it was counting the number of 'e's in the actual code. The aruaments are in elements 1, 2, etc, depending on how many you pass in on the command line.

The final line in the code calls the method in a print statement to print the number of 'e's in an aesthetically pleasing manner.

To call the program form the command line where the file name is 'moby-dick.txt' you would input the following command:
    python es.py moby-dick.txt
(es.py is the name of the program)