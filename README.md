# Career Salary Estimator
U.S. News presented a list of the Top 100 Careers in 2021, which featured many new and exciting options like *Data Scientist*, but also old-reliable one's like *Accountant* or *Physician*.  This project aims to find a relationship between the average salary of the Top 50 Careers from the former list and numerous variables that pertain to the job posting.  Assuming these relationship can be identified, we aim to exploit the underlying patterns that drive salary with the hopes of developing a regression model that can accurately predict the average salary of various career paths.  

## Overview
* Built a tool (MAE ~ $16,000) that can estimate the salary of the [Top 50 Careers according to U.S. News for 2021](https://money.usnews.com/careers/best-jobs/rankings/the-100-best-jobs).
* Utilizing [Selenium](https://www.selenium.dev), web scraped 1,000 job postings for each of the 50 Top Careers from [Glassdoor.com](https://www.glassdoor.com/index.htm).  In total, there were 48,522 data records were scraped from the platform, capturing features relating to the job posting and the company.
* Analyzed the scraped data from Glassdoor.com focusing on variables that can offer insights relating to the certain relationships that may exist with our target variable of *average salary*.
* Performed feature engineering on various columns to enhance the information we captured from Glassdoor.  For instance, we computed our dependent variable, *Average Salary* from the *Minimum* and *Maximum Salary* columns, taking into account if our data records were per hour, or annually.   
* Implemented exhaustive hyperparameter tuning of our Random Forest Regression model to arrive at the best performance, according to mean absolute error.  
* Developed a web application utilizing [Streamlit](https://streamlit.io) to allow for users to input values for our independent variables.  The web app then utilizes the serialized Random Forest Regression model to make predicts on the user inputted data.

## Demo of Web Application
You can of course interact with the Web Application yourself [here](https://share.streamlit.io/yiannimercer/career_salary_estimator/main/app.py)!
![Demo](https://github.com/yiannimercer/career_salary_estimator/blob/main/streamlit-app-2021-11-20-14-11-08.gif)

## Code and Resources Used
* See requirements.txt for a list of Python libraries that were utilized
* [Initial Glassdoor Web Scraper](https://github.com/arapfaik/scraping-glassdoor-selenium) (Script was edited due to the HTML code of Glassdoor being updated since this repository was finalized)
* [Initial Project Inspiration](https://www.youtube.com/watch?v=MpF9HENQjDo&list=RDCMUCiT9RITQ9PW6BhXK0y2jaeg&index=3) (Scarping Data Scientist Job Postings)
* [Deploying a Model Using Pickle and Streamlit](https://www.analyticsvidhya.com/blog/2020/12/deploying-machine-learning-models-using-streamlit-an-introductory-guide-to-model-deployment/)

## Data Collection
After updating the web scraper that was previously developed to the most recent (Nov, 2021) HTML Code that Glassdoor is using, the following variables were collected for each job posting:

* *Job Title* - Title of the Job Posting on Glassdoor (E.g., Data Scientist, Dental Hygienist)
* *Salary Estimate* - The Glassdoor provided average salary estimate based on previous employees in the same company and/or position who have reported their earnings to the platform.  (E.g., Employer Provided Salary: $80K - $100K)
* *Job Description* - A brief description of the job, responsibilities, and other need to know's that the company has chosen to share.
* *Company Rating* - A float data type representing the company's average rating, on a scale from 1.0 to 5.0 (E.g., 3.7)
* *Company Name* - The name of the company who is offering the job (E.g., Amazon.com Services LLC)
* *Location* - The location of where the job is being offered (E.g., Sandy, TX)
* *Size* - The size of the company as a whole. (E.g., 10000+ Employees)
* *Founded* - The year the company was founded (E.g., 1994)
* *Type of Ownership* - A string variable indicating if the company is public, private, school/university, government, etc. (E.g., Company - Public)
* *Industry* - The industry the company is in (E.g., Internet)
* *Sector* - The sector the company is in (E.g., Information Technology)
* *Revenue* - The revenue the company earns each fiscal year (E.g., $10+ Billion)

Additionally, various features were engineered or appended to the data frame that we developed.  Below is a list of these features.
