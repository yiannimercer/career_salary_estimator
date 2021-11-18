#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 15:38:59 2021

@author: yiannimercer
"""

import glassdoor_web_scraper as gs
import pandas as pd 
import os

# Current Working Directory (where the chromedriver should be located)
cwd = os.getcwd()

# Append the chromedriver to the end of the cwd path
path = cwd +'/chromedriver'

# Top Careers in American 2021 According to U.S. News

careers = ['Physician Assistant','Software Developer','Nurse Practitioner',
'Health Services Manager','Physician','Statistician','Speech Language Pathologist',
'Data Scientist','Dentist','Veterinarian','Orthodontist','IT Manager',
'Physicial Therapist Assistant','Anesthesiologist','Information Security Analyst',
'Substance Abuse Counselor','Behavioral Disorder Counselor','Financial Manager',
'Oral Surgeon','Occupational Therapist','Marriage and Family Therapist',
'Physical Therapist','Orthotist and Prosthetist','Mechanical Engineer','Financial Advisor',
'Cartographer','Pilot','Psychiatrist','Home Health Aide','Personal Care Aide',
'Operations Research Analyst','Marketing Manager','Dental Hygienist',
'Diagnostic Medical Sonographer','Wind Turbine Technician','Prosthodontist',
'Genetic Counselor','Registered Nurse','Lawyer','Nurse Anesthetist','Phlebotomist',
'Interpreter and Translator','Gynecologist','Surgeon','Chiropractor','Petroleum Engineer',
'Podiatrist','Computer Systems Analyst','Optometrist','Mathematician','Compliance Officer']

# Path to place Data Sets in

data_path = cwd +'/data_files/'

# Iterate through each job and scrape data and export csv to data_files directory

for i in range(len(careers)):
    df = gs.get_jobs(careers[i],1000,False,path,10)
    df.to_csv(data_path + careers[i].replace(' ','_') + '.csv')


