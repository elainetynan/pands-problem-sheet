# lab11q01to06.py
#
# This program creates a list of lists and prints out the dataFrame

# Author: Elaine Tynan

import pandas as pd

listData= [
    ['John', 'math', 23],
    ['John', 'programming', 66],
    ['Mary', 'math', 45],
    ['Mary', 'programming', 33],
    ['Mark', 'SIEM', 57],
    ['Mark', 'programming', 70],
    ['Mark', 'math', 73],
    ['John', 'programming', 61]
]

df = pd.DataFrame(listData, columns=['name','subject','grade'])
print(df.head(3))
print("~~~~~~~~~~~~~~~~~~~~~")
print()

print(df.describe())
print("~~~~~~~~~~~~~~~~~~~~~")
print()

print(type(df.describe()))
print("~~~~~~~~~~~~~~~~~~~~~")
print()

path = "./data/"
#csvFilename = path+'grades.csv'
csvFilename = 'grades.csv'
df.to_csv(csvFilename)

#excelFilename = path+'grades.xlsx'
excelFilename = 'grades.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')

with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name='summary')

#mean = df.describe().loc['mean','grade']
#print(mean)
# or
mean = df['grade'].mean()
print(mean)