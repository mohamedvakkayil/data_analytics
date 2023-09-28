'''Objectives: 
•	Apply principles and practices of data exploration, manipulation and preprocessing
•	Program at a basic level using R programming language
•	Explore data analytics techniques such as correlation, visualization such as scatter plots,
 pie chart, table, distribution of data, and outlier analysis.
Requirements: 
1.	Create a new single data set that can be used to output a table that lists the number of persons injured 
or killed in traffic accidents in each neighbourhood of Toronto in the last 4 years. (You will need to extract 
the following information: Year, vehicles in the street, district, and Neighbourhood)
2.	Write a sequence of code that shows the total vehicles in the street for each district for the last 4 
years during the accidents.
3.	Write a sequence of code that lists the top 5 neighbourhoods with the highest average number of 
vehicles in the streets.
'''

import pandas as pd

pd.set_option('display.max_colwidth', None) 

'''1.	Create a new single data set that can be used to output a table that lists the number of persons injured 
or killed in traffic accidents in each neighbourhood of Toronto in the last 4 years. (You will need to extract 
the following information: Year, vehicles in the street, district, and Neighbourhood)'''

column_mapping = [
    'YEAR',
    'DISTRICT',
    'VEHICLE_IN_STREET',
    'NEIGHBOUR']


'''Reading 2015_KSI.csv'''
data_types = {
    'YEAR': int,
    'DISTRICT': str,
    'VEHICLES_IN_STREET': int,
    'NEIGHBOURHOOD': str
    }
df = pd.read_csv('2015_KSI.csv')
df = df.astype(data_types)

df_new = df.filter(['YEAR','DISTRICT','VEHICLES_IN_STREET','NEIGHBOURHOOD'])
df_new = df_new.astype(data_types)


df_new.columns = column_mapping

'''Reading 2016_KSI.csv'''
data_types2 = {
    'YEAR': int,
    'DISTRICT': str,
    'VEHICLE_STREET': int,
    'NEIGHBOUR': str
    }

df = pd.read_csv('2016_KSI.csv')
df = df.astype(data_types2)

df = df.filter(['YEAR','DISTRICT','VEHICLE_STREET','NEIGHBOUR'])
df.columns = column_mapping

df_new= pd.concat([df_new, df])

'''Reading 2017_KSI.csv'''
data_types3 = {
    'YEAR': int,
    'DISTRICT': str,
    'VEHICLE_IN_STREET': int,
    'NEIGHBOURHOOD': str
    }
df = pd.read_csv('2017_KSI.csv')
df = df.astype(data_types3)

df = df.filter(['YEAR','DISTRICT','VEHICLE_IN_STREET','NEIGHBOURHOOD'])
df.columns = column_mapping

df_new= pd.concat([df_new, df])

'''Reading 2018_KSI.csv'''

df = pd.read_csv('2018_KSI.csv')
df = df.astype(data_types3)

df = df.filter(['YEAR','DISTRICT','VEHICLE_IN_STREET','NEIGHBOURHOOD'])
df.columns = column_mapping

df_new= pd.concat([df_new, df])

print(df_new)