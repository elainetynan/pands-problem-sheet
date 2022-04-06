# pands-problem-sheet
Weekly problem sheets

09/03/2022
This week I firstly made changes to my existing repository based on feedback from Andrew. The changes are as folows:
    I updated the Readme file (included references where appropriate as well as other minor changes)
    I removed all folders and just put all the weekly taks into the repository directly.
    I renamed Task05.py to weekday.py
    I made changes to some of the weekly tasks (secondString.py & weekday.py) based on the feedback recieved. These changes are documented in the comments in each python program.

04/03/2022
I was sick with covid the last 2 weeks (Weeks 5 & 6) I'm not sure if the instructions for the problem sheet went up before that, if so I don't know how I missed them. If it was in week 5 or 6, I did do the work but having gone back over it, I realise my head really wasn't right at the time.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Week 02
I didn't need to do any research on how to calculate the bmi as Andrew has it on the Moodle page in the task description. I did however, do some research on how format output in python. I found a nice resource on geeksforgeeks.org at this address:
https://www.geeksforgeeks.org/python-output-formatting/

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

I did some research on the newton method. Immediately I found the answer invarious languages. I read the java code to find out how to do the calculation and then with that knowledge wrote the python code. See the link here:
https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.

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

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Week 08
This week I did the plottask.py weekly task.
Here I was to create a plots with 2 plots on it for the x axis values from 0 to 4 and the g(x) = x squared and h(x) = x cubed.
I did some research on formatting the plot title and how to rotate the axis labels and included the links for reference in the code.
This is definitely an 'instant gratification' type of learning. Seeing the graphs appear with such a good finish but from such little code was very rewarding.

In plottask.py I firstly set the min and max x values. Numpy uses the range from the min up to but not including the max value so I put in the values 0 & 5 to get the values from 0 to 4.
Next I got the range of values for f(x), g(x) and h(x). I ploted g(x) with the f(x) and then the h(x) with the f(x) on 1 plot. I set labels and colours for each.
Next I turned on the minor ticks and set the axes labels, rotating the y-axis label so that it is horizontal.
The last part is to set the Title of the plot. BEfore doing this I set up a dictionary to format the text of the title. The dict stores the font family, colour, weight and size. Once this was set up I set the title, passing this dict in for formatting.
The final thing was to show and/or save the plot.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Week 09
This week we worked with errors, testing and logging.
It was really useful to be able to test the code in the current class without having to remove the code or comment it out afterwards. Having come form a Java background I am not aware of a way to do this in Java so I reallly liked this feature in python. The assert statement works in a similar fashion to the Java Assert class but I would ony previously have used it in formal testing in Java.
Another thing that s really useful is the logging feature. It is useful to change the level of logging based on what you are doing. Again, it saves you the effort of having to remove or comment out code for production.

When doing the work for lab 9, I firstly set up the definition of the function in the file called myFunctions.py, it initially returned an empty list. This allowed me to set up the tests passing in the values 7, 11, 0 and 1. I also set up lists of the expected output for each value passed in (7, 11, 0 & 1). Next I used the assert statements to verify the returned list from the fibonacci function matched the expected output for each value passed in. Initially 3 of 4 of these tests failed as the function was simply returning an empty list. The call where 0 was passed in actually passes because the output should be an empty list.

Once the test were set up and run while the code was not complete (and therefore failing) I was ready to start wriing the code for the fibonacci series.
In the function we start with setting up the first 2 values (a=0 & b=1) and teh list with the first value (0) already in it. Then we loop through all of the values up to the numbers passed in and append the next value. First time through the loop that is 1 as b has been set to 1. After this, a is set equal to the value stoore in b abd b becobes equal to the value of a plus b. This is done in a shorthand way that allows it all to happen in 1 statment, if it were to be done seperate a temporary valriable would be required as follows:
    tmp = a
    a = b
    b = tmp + b

Next the test for a negative number was put in place. In the fibonacci function if a negative value (less than 0) is passed in, a ValueError is returned so we must enclose our test with a nagative number in a try-except block, which displays the fail message if a ValueError is returned. This is similar to how a try-catch block works in Java when an exception is thrown.

Finally the last check is for the value 0 being passed in, in this case an empty list is simply returned.

At this point the tests are run again and should pass, meaning that the lists returned each time match the expected output(list)

Finally the file useFib.py is created to ask the user to enter a value which is then passed to the function and display the corresponding fibonacci numbers. This allowed us to keep the testing and logging in the original code but when called from elsewhere (useFib.py) it does not show any of the logging, etc, just the desired output.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Week 10
This week were were working with objects. I have experience with object oriented programming through Java and C# so the terminology was familiar to me. To me, the differences I observed compared to Java are:
Everything is done inside classes, whereas in Python classes are used only when needed. I ca see the advantages to this, especially for smaller pieces of code but it still feels a little strange to me.
The other thing that is done differnetly is that the constructor is always called __init__ as opposed to the same name as the class in Java and I must remember top always pass in self so that I can access the object. Personally I prefer the use of the keywords super and this from Java, but that is probably becuase I am more familiar with them.
Another difference is that by using self. anywhere in the code we can set up attributes. In java attributes are generally all listed together, often at the top of the class which makes it very easy to see the structure of the object/class at a glance.


In the lab we created a simple Timesheetentry class that had 3 attributes that were set in the construre using the parameters passed in. The attributes were project, start and duration.
We then created the __str__ function (similar to toString in Java) to return a string representation of the class/object. Finally in this part of the lab we did some testing to create some TimesheetEntry objects and display them using the __str_ function.

Next we created another class called Employee, this class had an attribute that was a list of TimesheetEntry objects (this is known as composition) it also had  2 attribtes for first and last name that were set in the constructor. Similar to the first class we also created a __str__ function that retuned a string of teh first and last names concatedated with a space between them. Then we did some testing to create some Employee objects and display them, again using the __str_ function. We checked that the first and last names were set using the assert statement.
Next we created a function that got the currect system time and created a Timesheet Entry object with the current datetime and added it to the list (the attribute) of Timesheetentry objects.
The next function gets the total time spent on all the TimesheetEntries by adding the duration of each Timesheetentry to a running total in a loop.
The last part of the lab is simply a test to create an employee, verify that the first and last name are set correctly, then log to Timesheet Entries, get the total time and display and verify it is correct.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Week 11
This week we looked at Pandas. This is a tool in python to analyse and manipulate data.
This seems like a really useful tool and with this and all the plotting functions we have seen this semester I can see why Python is so popular in data analytics.

This lab is broken into 2 parts.

In question 1 to 6 we initially create data (a list of lists) and with this data we set up a dataframe (a adataframe is a data structure that allows you to store data in rows and columns, like an excel sheet or a table in a database). When setting up the dataframe we give names to the columns, which is a really useful feature.
We then display information from the dataframe using various functions in DAtaframe. Firstly we used the ehad function (passing in 3) to display the first 3 rows of data.
Next we use the describe function to print out various descriptive statistics such as mean, count, standard deviation, etc.
In the next print command we display the type of data class that the decribe function is stored in ('pandas.core.frame.DataFrame').
NExt we send the dataframe to a csv file, with a given name and it creates teh file in the correct location (according to path) with the given name. Similarly we then send the dataframe to an excel file.
Finally in the first part we get the mean of the grade abd display it.

In questions 7 to 16 we again create a dataframe beut this time we get the data from a log file called access.log. We inform the Pandas read_csv function that the fields are separated by a space, that the file has no header and give it a list of column names to use. Next we drop any columns that just have dashed in them as this is not useful data. Next we format the time to make it look more aesthetically pleasing by dropping the square brackets at the start and end. WE then looked at the first 10 rows using iloc (which stands for integer location ref: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html). Then we format the date so that it prints out the date followed by the time (more on this at: https://docs.python.org/3/library/datetime.html#strftime-andstrptime-behavior).
Then we looked at getting data from the dataframe between 2 dates. This can be done in at least 3 ways. The first wasy was using the loc function, the second using the series between function, the third and final way was by setting the index to the date column which is obviously really useful to be able to change the index when needed.
Finally we got the sample average (mean) every 30 minutes and plotted it.
As an extra task we were asked to plot a rolling average over 6 hours for every hours. I have tried this and have managed to get some plots but I'm not sure if tehy are correct.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
