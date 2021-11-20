# Career Salary Estimator

## Overview
* Built a tool (MAE ~ $16,000) that can estimate the salary of the [Top 50 Careers according to U.S. News for 2021](https://money.usnews.com/careers/best-jobs/rankings/the-100-best-jobs).
* Utilizing [Selenium](https://www.selenium.dev), web scraped 1,000 job postings for each of the 50 Top Careers from [Glassdoor.com](https://www.glassdoor.com/index.htm).  In total, there were 48,522 data records were scraped from the platform, capturing features relating to the job posting and the company.
* Performed feature engineering on various columns to enhance the information we captured from Glassdoor.  For instance, we computed our dependent variable, *Average Salary* from the *Minimum* and *Maximum Salary* columns, taking into account if our data records were per hour, or annually.   
* Implemented exhaustive hyperparameter tuning of our Random Forest Regression model to arrive at the best performance, according to mean absolute error.  
* Analyzed the scraped data from Glassdoor.com focusing on variables that can offer insights relating to the certain relationships that may exist with our target variable of *average salary*.
