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
    
    #Create user input field to enter the data required
    simplified_job_title = st.selectbox("What is the Official Job Title?",('Veterinarian'
                                                ,'Dentist'
                                                ,'Mechanical Engineer'
                                                ,'Information Security Analyst'
                                                ,'Marriage and Family Therapist'
                                                ,'Computer Systems Analyst'
                                                ,'Nurse Practitioner'
                                                ,'Data Scientist'
                                                ,'Software Developer'
                                                ,'Substance Abuse Counselor'
                                                ,'Statistician'
                                                ,'Petroleum Engineer'
                                                ,'Physical Therapist'
                                                ,'Home Health Aide'
                                                ,'Physician'
                                                ,'Gynecologist'
                                                ,'Chiropractor'
                                                ,'Physician Assistant'
                                                ,'Dental Hygienist'
                                                ,'IT Manager'
                                                ,'Lawyer'
                                                ,'Oral Surgeon'
                                                ,'Financial Manager'
                                                ,'Nurse Anesthetist'
                                                ,'Health Services Manager'
                                                ,'Financial Advisor'
                                                ,'Optometrist'
                                                ,'Orthodontist'
                                                ,'Diagnostic Medical Sonographer'
                                                ,'Personal Care Aide'
                                                ,'Operations Research Analyst'
                                                ,'Wind Turbine Technician'
                                                ,'Genetic Counselor'
                                                ,'Prosthodontist'
                                                ,'Occupational Therapist'
                                                ,'Orthotist and Prosthetist'
                                                ,'Behavioral Disorder Counselor'
                                                ,'Psychiatrist'
                                                ,'Phlebotomist'
                                                ,'Registered Nurse'
                                                ,'Marketing Manager'
                                                ,'Compliance Officer'
                                                ,'Interpreter and Translator'
                                                ,'Anesthesiologist'
                                                ,'Surgeon'
                                                ,'Mathematician'
                                                ,'Pilot'
                                                ,'Speech Language Pathologist'
                                                ,'Podiatrist'))
    Rating = st.selectbox('Rating of the Company on Glassdoor.com',(1.0,2.0,3.0,4.0,5.0))
    Size = st.selectbox("Size of the Company",("-1 - Non Applicable"
                                ,'10000+ Employees'
                                ,'51 to 200 Employees'
                                ,'1 to 50 Employees'
                                ,'1001 to 5000 Employees'
                                , 'Unknown'
                                , '501 to 1000 Employees'
                                , '5001 to 10000 Employees'
                                , '201 to 500 Employees'))
    Type_of_ownership  = st.selectbox("Type of Ownership of the Company",('-1 - Non Applicable'
                                                            ,'Company - Private'
                                                            ,'Company - Public'
                                                            ,'Nonprofit Organization'
                                                            ,'Hospital'
                                                            ,'Subsidiary or Business Segment'
                                                            ,'Unknown'
                                                            ,'College / University'
                                                            ,'Private Practice / Firm'
                                                            ,'Government'
                                                            ,'Contract'
                                                            ,'Self-employed'
                                                            ,'Franchise'
                                                            ,'School / School District'))
    Industry = st.selectbox("Industry the Company Currently Is In",('Unknown'
                                        ,'Health Care Services & Hospitals'
                                        ,'Staffing & Outsourcing'
                                        ,'Colleges & Universities'
                                        ,'Investment Banking & Asset Management'
                                        ,'Computer Hardware & Software'
                                        ,'IT Services'
                                        ,'Aerospace & Defense'
                                        ,'Insurance Carriers'
                                        ,'Energy'
                                        ,'Federal Agencies'
                                        ,'Biotech & Pharmaceuticals'
                                        ,'Banks & Credit Unions'
                                        ,'Social Assistance'
                                        ,'Consulting'
                                        ,'Internet'
                                        ,'Enterprise Software & Network Solutions'
                                        ,'Industrial Manufacturing'
                                        ,'Electrical & Electronic Manufacturing'
                                        ,'Research & Development'
                                        ,'Legal'
                                        ,'Veterinary Services'
                                        ,'K-12 Education'
                                        ,'Insurance Agencies & Brokerages'
                                        ,'Consumer Products Manufacturing'
                                        ,'Architectural & Engineering Services'
                                        ,'Oil & Gas Services'
                                        ,'Food & Beverage Manufacturing'
                                        ,'Lending'
                                        ,'Telecommunications Services'
                                        ,'Health, Beauty, & Fitness'
                                        ,'Real Estate'
                                        ,'Advertising & Marketing'
                                        ,'Building & Personnel Services'
                                        ,'Brokerage Services'
                                        ,'Transportation Equipment Manufacturing'
                                        ,'Accounting'
                                        ,'Transportation Management'
                                        ,'Department, Clothing, & Shoe Stores'
                                        ,'Airlines'
                                        ,'Logistics & Supply Chain'
                                        ,'Oil & Gas Exploration & Production'
                                        ,'Health Care Products Manufacturing'
                                        ,'Utilities'
                                        ,'Financial Transaction Processing'
                                        ,'Construction'
                                        ,'Health Fundraising Organizations'
                                        ,'Museums, Zoos & Amusement Parks'
                                        ,'Hotels, Motels, & Resorts'
                                        ,'Cable, Internet & Telephone Providers'
                                        ,'Chemical Manufacturing'
                                        ,'Membership Organizations'
                                        ,'Vehicle Dealers'
                                        ,'Security Services'
                                        ,'Miscellaneous Manufacturing'
                                        ,'Motion Picture Production & Distribution'
                                        ,'Consumer Product Rental'
                                        ,'Metal & Mineral Manufacturing'
                                        ,'Financial Analytics & Research'
                                        ,'TV Broadcast & Cable Networks'
                                        ,'Casual Restaurants'
                                        ,'Preschool & Child Care'
                                        ,'Food Production'
                                        ,'General Repair & Maintenance'
                                        ,'Wholesale'
                                        ,'Consumer Electronics & Appliances Stores'
                                        ,'Pet & Pet Supplies Stores'
                                        ,'Catering & Food Service Contractors'
                                        ,'Municipal Governments'
                                        ,'State & Regional Agencies'
                                        ,'Publishing'
                                        ,'Drug & Health Stores'
                                        ,'Commercial Printing'
                                        ,'Education Training Services'
                                        ,'Grocery Stores & Supermarkets'
                                        ,'Camping & RV Parks'
                                        ,'Fast-Food & Quick-Service Restaurants'
                                        ,'Travel Agencies'
                                        ,'Trucking'
                                        ,'Laundry & Dry Cleaning'
                                        ,'Business Service Centers & Copy Shops'
                                        ,'Toy & Hobby Stores'
                                        ,'Sports & Recreation'
                                        ,'Express Delivery Services'
                                        ,'Moving Services'
                                        ,'Home Furniture & Housewares Stores'
                                        ,'Other Retail Stores'
                                        ,'Beauty & Personal Accessories Stores'
                                        ,'Gambling'
                                        ,'Parking Lots & Garages'
                                        ,'Grantmaking Foundations'
                                        ,'Video Games'
                                        ,'Music Production & Distribution'
                                        ,'Sporting Goods Stores'
                                        ,'Gas Stations'
                                        ,'Media & Entertainment Retail Stores'
                                        ,'Mining'
                                        ,'Commercial Equipment Repair & Maintenance'
                                        ,'General Merchandise & Superstores'
                                        ,'Home Centers & Hardware Stores'))
    
    Sector = st.selectbox("Sector the Company Currently Is In",('Unknown'
                                    ,'Health Care'
                                    ,'Business Services'
                                    ,'Information Technology'
                                    ,'Finance'
                                    ,'Manufacturing'
                                    ,'Education'
                                    ,'Oil, Gas, Energy & Utilities'
                                    ,'Insurance'
                                    ,'Aerospace & Defense'
                                    ,'Non-Profit'
                                    ,'Government'
                                    ,'Biotech & Pharmaceuticals'
                                    ,'Consumer Services'
                                    ,'Accounting & Legal'
                                    ,'Retail'
                                    ,'Transportation & Logistics'
                                    ,'Telecommunications'
                                    ,'Travel & Tourism'
                                    ,'Real Estate'
                                    ,'Construction, Repair & Maintenance'
                                    ,'Media'
                                    ,'Arts, Entertainment & Recreation'
                                    ,'Restaurants, Bars & Food Services'
                                    ,'Agriculture & Forestry'
                                    ,'Mining & Metals'))
    
    Revenue = st.selectbox("Revenue of the Company",('-1 - Not Sure'
                                    ,'Unknown / Non-Applicable'
                                    ,'$10+ billion (USD)'
                                    ,'$100 to $500 million (USD)'
                                    ,'$2 to $5 billion (USD)'
                                    ,'$25 to $50 million (USD)'
                                    ,'$10 to $25 million (USD)'
                                    ,'$1 to $5 million (USD)'
                                    ,'$1 to $2 billion (USD)'
                                    ,'$50 to $100 million (USD)'
                                    ,'$5 to $10 billion (USD)'
                                    ,'$500 million to $1 billion (USD)'
                                    ,'$5 to $10 million (USD)'
                                    ,'Less than $1 million (USD)'))
    
    employer_provided = st.selectbox("Does the Employer Provide Salary on Glassdoor.com?",("Yes","No"))
    
    job_state = st.selectbox("What State is the Job Located In?",('CA'
                                        ,'Remote'
                                        ,'IL'
                                        ,'TX'
                                        ,'FL'
                                        ,'NY'
                                        ,'MA'
                                        ,'WA'
                                        ,'NC'
                                        ,'VA'
                                        ,'NJ'
                                        ,'PA'
                                        ,'CO'
                                        ,'AZ'
                                        ,'GA'
                                        ,'MD'
                                        ,'OH'
                                        ,'MI'
                                        ,'MN'
                                        ,'MO'
                                        ,'TN'
                                        ,'OR'
                                        ,'NV'
                                        ,'CT'
                                        ,'WI'
                                        ,'UT'
                                        ,'OK'
                                        ,'United States'
                                        ,'NH'
                                        ,'KY'
                                        ,'IN'
                                        ,'DC'
                                        ,'NM'
                                        ,'NE'
                                        ,'ME'
                                        ,'LA'
                                        ,'MT'
                                        ,'SC'
                                        ,'MS'
                                        ,'KS'
                                        ,'HI'
                                        ,'ND'
                                        ,'AK'
                                        ,'AL'
                                        ,'IA'
                                        ,'ID'
                                        ,'RI'
                                        ,'WV'
                                        ,'VT'
                                        ,'AR'
                                        ,'WY'
                                        ,'DE'
                                        ,'GU'
                                        ,'PR'
                                        ,'VI'
                                        ,'SD'))
    
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
        link = "#### For more information on this career, check out Glassdoor's Information [Page](https://www.glassdoor.com/Search/results.htm?keyword={})".format(simplified_job_title.replace(' ',''))
        st.markdown(link,unsafe_allow_html=True)
 
if __name__=='__main__': 
    main()    
