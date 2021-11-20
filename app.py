#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 08:41:10 2021

@author: yiannimercer
"""


import pickle 
import streamlit as st
import numpy as np
import pandas as pd

# Load in the trained model
pickle_in = open('regressor.pkl','rb')
regressor = pickle.load(pickle_in)

@st.cache()

# Define function which will the prediction using data the user inputs

def prediction(Rating,Size,Type_of_ownership,Industry,Sector,Revenue,employer_provided,job_state,age,simplified_job_title,seniority):
    import numpy as np
    import pandas as pd
    
    if Size == "-1 - Non Applicable":
        Size = '-1'
    
    if Type_of_ownership == '-1 - Non Applicable':
        Type_of_ownership = '-1'
    
    if Industry == 'Unknown':
        Industry = '-1'
    
    if Sector == 'Unknown':
        Sector = '-1'
        
    if Revenue == '-1 - Not Sure':
        Revenue = '-1'
        
    if employer_provided == "Yes":
        employer_provided = 1
    else:
        employer_provided = 0
        
    if int(age) > 0:
        age = int(age)
    else:
        age = -1
        
    if seniority == "Senior":
        seniority = 'senior'
    elif seniority == "Junior":
        seniority = 'jr'
    else:
        seniority = 'na'
    
    # pre-process user input into our 275 column ingestion pipeline
    df = pd.read_csv("eda_data.csv")
    #Create column to keep track of our user data
    df['to_predict'] = 0
    #Modeling DataFrame
    df_model = df[['Rating','Size','Type of ownership','Industry','Sector','Revenue','employer_provided','job_state','age',
                   'simplified_job_title','seniority','to_predict']]
    #Append User Inputs
    df_model.loc[len(df_model.index)] = [Rating,Size,Type_of_ownership,Industry,Sector,Revenue,employer_provided,job_state,age,simplified_job_title,seniority,1]
    
    # Get Dummy Data 
    df_dum = pd.get_dummies(df_model)
    #Filter on our engineered column to only user inputs
    data_to_predict_df = df_dum[df_dum['to_predict']==1]
    #Drop our engineered column
    data_to_predict_df = data_to_predict_df.drop(['to_predict'],axis=1)
    data_to_predict = np.array([data_to_predict_df]).reshape(1,-1)

    # Make predicition of avg salary
    prediction = regressor.predict(data_to_predict)
    return prediction

    #Define Web Page
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">A Machine Learning Apporach of Estimating Career Salaries</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp,unsafe_allow_html = True)
    st.write("The following application utlizes Glassdoor.com and the large amount of data that resides on their platform. This application harnesses 1,000 job postings for each of the Top 50 Careers of 2021, according to U.S. News.  In total, nearly 50,000 data records were used to optmized a Random Forest Regerssion Model that utlized GridSearchCV to Hypertune a variety of parameters. I hope you enjoy the application and make some interesting insights!  ")
    st.write("")
    #Create user input field to enter the data required
    simplified_job_title = st.selectbox("What is the Official Job Title?",('Anesthesiologist'
                                                                            ,'Behavioral Disorder Counselor'
                                                                            ,'Chiropractor'
                                                                            ,'Compliance Officer'
                                                                            ,'Computer Systems Analyst'
                                                                            ,'Data Scientist'
                                                                            ,'Dental Hygienist'
                                                                            ,'Dentist'
                                                                            ,'Diagnostic Medical Sonographer'
                                                                            ,'Financial Advisor'
                                                                            ,'Financial Manager'
                                                                            ,'Genetic Counselor'
                                                                            ,'Gynecologist'
                                                                            ,'Health Services Manager'
                                                                            ,'Home Health Aide'
                                                                            ,'IT Manager'
                                                                            ,'Information Security Analyst'
                                                                            ,'Interpreter and Translator'
                                                                            ,'Lawyer'
                                                                            ,'Marketing Manager'
                                                                            ,'Marriage and Family Therapist'
                                                                            ,'Mathematician'
                                                                            ,'Mechanical Engineer'
                                                                            ,'Nurse Anesthetist'
                                                                            ,'Nurse Practitioner'
                                                                            ,'Occupational Therapist'
                                                                            ,'Operations Research Analyst'
                                                                            ,'Optometrist'
                                                                            ,'Oral Surgeon'
                                                                            ,'Orthodontist'
                                                                            ,'Orthotist and Prosthetist'
                                                                            ,'Personal Care Aide'
                                                                            ,'Petroleum Engineer'
                                                                            ,'Phlebotomist'
                                                                            ,'Physical Therapist'
                                                                            ,'Physician'
                                                                            ,'Physician Assistant'
                                                                            ,'Pilot'
                                                                            ,'Podiatrist'
                                                                            ,'Prosthodontist'
                                                                            ,'Psychiatrist'
                                                                            ,'Registered Nurse'
                                                                            ,'Software Developer'
                                                                            ,'Speech Language Pathologist'
                                                                            ,'Statistician'
                                                                            ,'Substance Abuse Counselor'
                                                                            ,'Surgeon'
                                                                            ,'Veterinarian'
                                                                            ,'Wind Turbine Technician'))
    Rating = st.selectbox('Rating of the Company on Glassdoor.com',(1.0,2.0,3.0,4.0,5.0))
    Size = st.selectbox("Size of the Company",("-1 - Non Applicable"
                                ,'1 to 50 Employees'
                                ,'51 to 200 Employees'
                                ,'201 to 500 Employees'
                                ,'501 to 1000 Employees'
                                ,'1001 to 5000 Employees'
                                ,'5001 to 10000 Employees'
                                ,'10000+ Employees'
                                , 'Unknown'))
    Type_of_ownership  = st.selectbox("Type of Ownership of the Company",('-1 - Non Applicable'
                                                            ,'College / University'
                                                            ,'Company - Private'
                                                            ,'Company - Public'
                                                            ,'Contract'
                                                            ,'Franchise'
                                                            ,'Government'
                                                            ,'Hospital'
                                                            ,'Nonprofit Organization'
                                                            ,'Private Practice / Firm'
                                                            ,'School / School District'
                                                            ,'Self-employed'
                                                            ,'Subsidiary or Business Segment'
                                                            ,'Unknown'))
    Industry = st.selectbox("Industry the Company Currently Is In",('Accounting'
                                                                    ,'Advertising & Marketing'
                                                                    ,'Aerospace & Defense'
                                                                    ,'Airlines'
                                                                    ,'Architectural & Engineering Services'
                                                                    ,'Banks & Credit Unions'
                                                                    ,'Beauty & Personal Accessories Stores'
                                                                    ,'Biotech & Pharmaceuticals'
                                                                    ,'Brokerage Services'
                                                                    ,'Building & Personnel Services'
                                                                    ,'Business Service Centers & Copy Shops'
                                                                    ,'Cable, Internet & Telephone Providers'
                                                                    ,'Camping & RV Parks'
                                                                    ,'Casual Restaurants'
                                                                    ,'Catering & Food Service Contractors'
                                                                    ,'Chemical Manufacturing'
                                                                    ,'Colleges & Universities'
                                                                    ,'Commercial Equipment Repair & Maintenance'
                                                                    ,'Commercial Printing'
                                                                    ,'Computer Hardware & Software'
                                                                    ,'Construction'
                                                                    ,'Consulting'
                                                                    ,'Consumer Electronics & Appliances Stores'
                                                                    ,'Consumer Product Rental'
                                                                    ,'Consumer Products Manufacturing'
                                                                    ,'Department, Clothing, & Shoe Stores'
                                                                    ,'Drug & Health Stores'
                                                                    ,'Education Training Services'
                                                                    ,'Electrical & Electronic Manufacturing'
                                                                    ,'Energy'
                                                                    ,'Enterprise Software & Network Solutions'
                                                                    ,'Express Delivery Services'
                                                                    ,'Fast-Food & Quick-Service Restaurants'
                                                                    ,'Federal Agencies'
                                                                    ,'Financial Analytics & Research'
                                                                    ,'Financial Transaction Processing'
                                                                    ,'Food & Beverage Manufacturing'
                                                                    ,'Food Production'
                                                                    ,'Gambling'
                                                                    ,'Gas Stations'
                                                                    ,'General Merchandise & Superstores'
                                                                    ,'General Repair & Maintenance'
                                                                    ,'Grantmaking Foundations'
                                                                    ,'Grocery Stores & Supermarkets'
                                                                    ,'Health Care Products Manufacturing'
                                                                    ,'Health Care Services & Hospitals'
                                                                    ,'Health Fundraising Organizations'
                                                                    ,'Health, Beauty, & Fitness'
                                                                    ,'Home Centers & Hardware Stores'
                                                                    ,'Home Furniture & Housewares Stores'
                                                                    ,'Hotels, Motels, & Resorts'
                                                                    ,'IT Services'
                                                                    ,'Industrial Manufacturing'
                                                                    ,'Insurance Agencies & Brokerages'
                                                                    ,'Insurance Carriers'
                                                                    ,'Internet'
                                                                    ,'Investment Banking & Asset Management'
                                                                    ,'K-12 Education'
                                                                    ,'Laundry & Dry Cleaning'
                                                                    ,'Legal'
                                                                    ,'Lending'
                                                                    ,'Logistics & Supply Chain'
                                                                    ,'Media & Entertainment Retail Stores'
                                                                    ,'Membership Organizations'
                                                                    ,'Metal & Mineral Manufacturing'
                                                                    ,'Mining'
                                                                    ,'Miscellaneous Manufacturing'
                                                                    ,'Motion Picture Production & Distribution'
                                                                    ,'Moving Services'
                                                                    ,'Municipal Governments'
                                                                    ,'Museums, Zoos & Amusement Parks'
                                                                    ,'Music Production & Distribution'
                                                                    ,'Oil & Gas Exploration & Production'
                                                                    ,'Oil & Gas Services'
                                                                    ,'Other Retail Stores'
                                                                    ,'Parking Lots & Garages'
                                                                    ,'Pet & Pet Supplies Stores'
                                                                    ,'Preschool & Child Care'
                                                                    ,'Publishing'
                                                                    ,'Real Estate'
                                                                    ,'Research & Development'
                                                                    ,'Security Services'
                                                                    ,'Social Assistance'
                                                                    ,'Sporting Goods Stores'
                                                                    ,'Sports & Recreation'
                                                                    ,'Staffing & Outsourcing'
                                                                    ,'State & Regional Agencies'
                                                                    ,'TV Broadcast & Cable Networks'
                                                                    ,'Telecommunications Services'
                                                                    ,'Toy & Hobby Stores'
                                                                    ,'Transportation Equipment Manufacturing'
                                                                    ,'Transportation Management'
                                                                    ,'Travel Agencies'
                                                                    ,'Trucking'
                                                                    ,'Unknown'
                                                                    ,'Utilities'
                                                                    ,'Vehicle Dealers'
                                                                    ,'Veterinary Services'
                                                                    ,'Video Games'
                                                                    ,'Wholesale'))
    
    Sector = st.selectbox("Sector the Company Currently Is In",('Accounting & Legal'
                                                                ,'Aerospace & Defense'
                                                                ,'Agriculture & Forestry'
                                                                ,'Arts, Entertainment & Recreation'
                                                                ,'Biotech & Pharmaceuticals'
                                                                ,'Business Services'
                                                                ,'Construction, Repair & Maintenance'
                                                                ,'Consumer Services'
                                                                ,'Education'
                                                                ,'Finance'
                                                                ,'Government'
                                                                ,'Health Care'
                                                                ,'Information Technology'
                                                                ,'Insurance'
                                                                ,'Manufacturing'
                                                                ,'Media'
                                                                ,'Mining & Metals'
                                                                ,'Non-Profit'
                                                                ,'Oil, Gas, Energy & Utilities'
                                                                ,'Real Estate'
                                                                ,'Restaurants, Bars & Food Services'
                                                                ,'Retail'
                                                                ,'Telecommunications'
                                                                ,'Transportation & Logistics'
                                                                ,'Travel & Tourism'
                                                                ,'Unknown'))
    
    Revenue = st.selectbox("Revenue of the Company",('Unknown / Non-Applicable'
                                     ,'Less than $1 million (USD)'
                                     ,'$1 to $5 million (USD)'
                                     ,'$5 to $10 million (USD)'
                                     ,'$10 to $25 million (USD)'
                                     ,'$25 to $50 million (USD)'
                                     ,'$50 to $100 million (USD)'
                                     ,'$100 to $500 million (USD)'
                                     ,'$500 million to $1 billion (USD)'
                                     ,'$1 to $2 billion (USD)'
                                     ,'$2 to $5 billion (USD)'
                                     ,'$5 to $10 billion (USD)'
                                     ,'$10+ billion (USD)'
                                     ,'-1 - Not Sure'))
    
    employer_provided = st.selectbox("Does the Employer Provide Salary on Glassdoor.com?",("Yes","No"))
    
    job_state = st.selectbox("What State is the Job Located In?",('AK'
                                                                ,'AL'
                                                                ,'AR'
                                                                ,'AZ'
                                                                ,'CA'
                                                                ,'CO'
                                                                ,'CT'
                                                                ,'DC'
                                                                ,'DE'
                                                                ,'FL'
                                                                ,'GA'
                                                                ,'GU'
                                                                ,'HI'
                                                                ,'IA'
                                                                ,'ID'
                                                                ,'IL'
                                                                ,'IN'
                                                                ,'KS'
                                                                ,'KY'
                                                                ,'LA'
                                                                ,'MA'
                                                                ,'MD'
                                                                ,'ME'
                                                                ,'MI'
                                                                ,'MN'
                                                                ,'MO'
                                                                ,'MS'
                                                                ,'MT'
                                                                ,'NC'
                                                                ,'ND'
                                                                ,'NE'
                                                                ,'NH'
                                                                ,'NJ'
                                                                ,'NM'
                                                                ,'NV'
                                                                ,'NY'
                                                                ,'OH'
                                                                ,'OK'
                                                                ,'OR'
                                                                ,'PA'
                                                                ,'PR'
                                                                ,'RI'
                                                                ,'Remote'
                                                                ,'SC'
                                                                ,'SD'
                                                                ,'TN'
                                                                ,'TX'
                                                                ,'UT'
                                                                ,'United States'
                                                                ,'VA'
                                                                ,'VI'
                                                                ,'VT'
                                                                ,'WA'
                                                                ,'WI'
                                                                ,'WV'
                                                                ,'WY'))
    
    age = st.number_input("How Old is the Company in Years? (Round to the near whole number)")

    seniority = st.selectbox("What (if applicable) is the Seniority Level of the Job?",("Senior","Junior","Not Applicable"))
    result = ""
    
    # Develop "Estimate Salary" so when clicked, the prediction function is run and the value is returned
    if st.button("Estimate Salary"):
        result = prediction(Rating,Size,Type_of_ownership,Industry,Sector,Revenue,employer_provided,job_state,age,simplified_job_title,seniority)
        st.warning("The below estimation is simply a prediction using various Machine Learning Techniques such as Random Forest Regression and GridSearchCV in the Sklearn Library.  Please take this into account when comparing predictions against your true values")
        result = float(result[0])
        result = str("${:.3f}".format(result))
        result = result.replace('.',',')
        st.success("Based off of the Random Forest Regression Model with Mean Absolute Error of ~ $16,400, and whose parameters were hypertuned using GridSearch CV, your estimated salary should be {}".format(result))
        link = "#### For more information on this career, check out Glassdoor's Information [Page](https://www.glassdoor.com/Search/results.htm?keyword={})".format(simplified_job_title.replace(" ","%20"))
        st.markdown(link,unsafe_allow_html=True)
    
    st.write("Please feel free to reach out to me regarding any questions, comments, or concerns!")
    st.write("Yianni John Mercer")
    st.write("DePaul University")
    st.write("Master's of Applied Statistics & Data Science")
    st.write("jmercer4@depaul.edu")
 
if __name__=='__main__': 
    main()    
