#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:11:21 2021

@author: yiannimercer
"""

# Importing Necessary Libraries
import pandas as pd
import numpy as np
import glob
import os


# Ingesting our collected data by iterating through each file, and then creating a list of data frames
path = os.getcwd()
all_files = glob.glob(path + "/data_collection/data_files/*.csv")




dfs = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=0)
    df['simplified_job_title'] = filename.split('/')[-1].replace('_',' ').replace('.csv','')
    dfs.append(df)


df = pd.concat(dfs, axis=0, ignore_index=True)

# Basic Understanding of Data
df.shape
df.head()
df.info()


# Items I need to address: 
    # Salary Parsing
    # Company Name Text Only
    # State Field
    # Age of Company 
    

##### SALARY PARSING ####

df['hourly'] = df['Salary Estimate'].astype(str).apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].astype(str).apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

#Removing the rows with no salary estimate as this is our target varaible
df = df[(df['Salary Estimate'] != '-1') & (df['Salary Estimate'].notnull())]

#Clearning Salary Estimate Column for the text and the '$' and 'K'
salary = df['Salary Estimate'].astype(str).apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

#Cleaning Salary Estimate column for the 'per hour' and 'K'
min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour',''))
min_hr = min_hr.apply(lambda x: x.lower().replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: x.split('-')[0])
df['max_salary'] = min_hr.apply(lambda x: x.split('-')[1] if len(x.split('-'))==2 else x)
df['min_salary'] = df['min_salary'].astype(int)
df['max_salary'] = df['max_salary'].astype(int)

## Average Salary -- Target Variable

df['avg_salary'] = df[['min_salary', 'max_salary']].mean(axis=1)
        

##### COMPANY NAME TEXT ONLY #####

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

##### STATE FIELD ####
df['job_state'] = df['Location'].astype(str).apply(lambda x: x.split(',')[1] if len(x.split(','))== 2 else x.split(',')[0]).str.strip()

##### AGE OF COMPANY #####

df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2021 - x)




df.to_csv("cleaned_df.csv")

