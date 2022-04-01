# lab11q07to16.py
#
# This program creates a list of lists and prints out the dataFrame

# Author: Elaine Tynan

import pandas as pd
import re
import matplotlib.pyplot as plt

path = './data/'
logFilename = path + 'access.log'

#df = pd.read_csv(logFilename, sep=' ', header= None)
#print(df)

# Set the column names
colNames= ('ip',
    'dash1',
    'userId',
    'time',
    'url',
    'status code',
    'size of response',
    'referer',
    'user agent',
    'dunno'
)
df = pd.read_csv(logFilename, sep=' ', header= None, names=colNames)

# Drop the columns that just contain dashed
df.drop(columns=['dash1', 'userId'], inplace=True)

# Remove the [] from time
# Use apply the function to each element in the column and return a series
# which I make the column equal to
df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())
'''
def getNewValue(x):
newvalue = re.search('[\w:/]+', x).group()
# do your stuff
return newvalue
df['time'] = df['time'].apply(getNewValue)
'''
#print(df.iloc[0]) # print the first 10 rows
#print(df.dtypes)

# this is not a normal date time format so we need to specify it
# https://docs.python.org/3/library/datetime.html#strftime-andstrptime-behavior
# https://pandas.pydata.org/pandasdocs/stable/reference/api/pandas.to_datetime.html?highlight=to_datetime
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

#print(df.iloc[0]) # print the first 10 rows
#print(df.dtypes)

########################################################
# Do the Analysis Get events that happen between 2 times

# way one use the loc function
#newdf = df.loc[(df['time'] > start_date) & (df['time'] < end_date)]

# way 2 use the series function between
#newdf = df[df.time.between(start_date, end_date)]

# way three set the index to the date column
# this give a whole pile of handy features
df = df.set_index(['time'])
newdf = df['2021/02/15 23:00':'2021/02/15 23:59:59']
#newdf = df.between_time('23:00', '23:59') # this is times every day

print (newdf)

# Sample the download sizes say every 30 Minutes
downloadSamples = df['size of response'].resample(rule='30Min').mean()
print(downloadSamples)

# Plot this in line plot
# more information on the documents
# https://pandas.pydata.org/pandasdocs/stable/getting_started/intro_tutorials/04_plotting.html
downloadSamples.plot()
plt.show()


#downloadSamples2 = df['size of response'].resample(rule='360Min').mean() # every 6 hours
#downloadSamples2 = df['size of response'].resample(rule='30Min').rolling(12).mean()
downloadSamples2 = df['size of response'].rolling(12).mean()
print(downloadSamples)
downloadSamples2.plot()
plt.show()