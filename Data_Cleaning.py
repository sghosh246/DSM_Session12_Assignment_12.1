# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:07:19 2018

@author: souravg

"""

"""
To Do : - It happens all the time: someone gives you data containing malformed strings, Python,
lists and missing data. How do you tidy it up so you can get on with the analysis?
Take this monstrosity as the DataFrame to use in the following puzzles:
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

1. Some values in the the FlightNumber column are missing. These numbers are meant
to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in
these missing numbers and make the column an integer column (instead of a float
column).
2. The From_To column would be better as two separate columns! Split each string on
the underscore delimiter _ to give a new temporary DataFrame with the correct values.
Assign the correct column names to this temporary DataFrame.
3. Notice how the capitalisation of the city names is all mixed up in this temporary
DataFrame. Standardise the strings so that only the first letter is uppercase (e.g.
"londON" should become "London".)
4. Delete the From_To column from df and attach the temporary DataFrame from the
previous questions.
5. In the RecentDelays column, the values have been entered into the DataFrame as a
list. We would like each first value in its own column, each second value in its own
column, and so on. If there isn't an Nth value, the value should be NaN.
Expand the Series of lists into a DataFrame named delays, rename the columns delay_1,
delay_2, etc. and replace the unwanted RecentDelays column in df with delays.
"""
import pandas as pd
import numpy as np
flights = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )','12. Air France', '"Swiss Air"']},columns=('From_To','FlightNumber','RecentDelays','Airline'))
    
#1. Missing values in FlightNumber column is incremented by 10 with starting value as 10045.
print("Missing values in FlightNumber column is incremented by 10 with starting value as 10045\n",'-'*87, sep='')
def create_list(x,y):
    for i in range(1,y):
        flights.loc[i,'FlightNumber'] = flights.loc[i-1,'FlightNumber']+10

flights['FlightNumber'].fillna(0, inplace=True)
flights['FlightNumber'] = flights['FlightNumber'].astype(int)
First_Flightnumber = flights.loc[0,'FlightNumber']
create_list(First_Flightnumber,len(flights.FlightNumber))
print(flights)
print('-'*87, sep='')
#2. Splitting From_To column with delimiter as underscore and assign those columns and their associated values to a temporary dataframe.
print("Splitting From_To column with delimiter as underscore and assign those columns and their associated values to a temporary dataframe\n",'-'*125, sep='')
def Fromsplitstring(str):
    return str.split('_')[0]

def Tosplitstring(str):
    return str.split('_')[1]

FromList = flights['From_To'].apply(Fromsplitstring)
ToList = flights['From_To'].apply(Tosplitstring)
#print(FromList)
#print(ToList)
temporary = pd.DataFrame()
temporary["From"] = FromList
temporary["To"] = ToList
print(temporary)
print('-'*125, sep='')
#3. Make first letter of From and To column values of temporary dataframe as uppercase.
print("Make first letter of From and To column values of temporary dataframe as uppercase\n",'-'*82, sep='')
temporary['From'] = list(map(lambda str : str.title(),temporary.From))
temporary['To'] = list(map(lambda str : str.title(),temporary.To))
print(temporary)
print('-'*82, sep='')
#4. Delete the From_To column from flights dataframe and attach the temporary dataFrame with flights.
print("Delete the From_To column from flights dataframe and attach the temporary dataFrame with flights\n",'-'*95, sep='')
flights.drop('From_To', axis=1, inplace=True)
flights = pd.concat([temporary, flights], axis=1)
print(flights)
print('-'*95, sep='')
#5. Split RecentDelays column like delay_1,delay_2, etc. based on the maximum no. of elements present in the list among other lists and replace the unwanted RecentDelays column in flights dataframe with delays.
print("Split RecentDelays column like delay_1,delay_2, etc. based on the maximum no. of elements present in the list among other lists and replace the unwanted RecentDelays column in flights dataframe with delays\n",'-'*205, sep='')
def DelayListParse(x):
    return len(x)   

DelayList = list(map(lambda x : len(x),flights.RecentDelays))
max_columns = max(DelayList)
#print(DelayList)
New_RecentDelays = []
Two_dim_RecentDelays = []
for outeritems in flights.RecentDelays:
    New_RecentDelays = outeritems
    count = len(outeritems)
    while(count<max_columns):
        New_RecentDelays.append(np.NaN)
        count +=1
    Two_dim_RecentDelays.append(New_RecentDelays)
#print(Two_dim_RecentDelays)
Delays = pd.DataFrame(Two_dim_RecentDelays)
column_list = []
for count in range(1,max_columns+1):
    column_list.append('delay_'+str(count))
Delays.columns = column_list
#print(Delays)
flights.drop('RecentDelays', axis=1, inplace=True)
flights = pd.concat([flights, Delays], axis=1)
print(flights)
print('-'*205, sep='')