parameters# Career Salary Estimator
U.S. News presented a list of the Top 100 Careers in 2021, which featured many new and exciting options like *Data Scientist*, but also old-reliable one's like *Accountant* or *Physician*.  This project aims to find a relationship between the average salary of the Top 50 Careers from the former list and numerous variables that pertain to the job posting.  Assuming these relationship can be identified, we aim to exploit the underlying patterns that drive salary with the hopes of developing a regression model that can accurately predict the average salary of various career paths.  

## Overview
* Built a tool (MAE ~ $16,000) that can estimate the salary of the [Top 50 Careers according to U.S. News for 2021](https://money.usnews.com/careers/best-jobs/rankings/the-100-best-jobs).
* Utilizing [Selenium](https://www.selenium.dev), web scraped 1,000 job postings for each of the 50 Top Careers from [Glassdoor.com](https://www.glassdoor.com/index.htm).  In total, there were 48,522 data records were scraped from the platform, capturing features relating to the job posting and the company.
* Analyzed the scraped data from Glassdoor.com focusing on variables that can offer insights relating to the certain relationships that may exist with our target variable of *average salary*.
* Performed feature engineering on various columns to enhance the information we captured from Glassdoor.  For instance, we computed our dependent variable, *Average Salary* from the *Minimum* and *Maximum Salary* columns, taking into account if our data records were per hour, or annually.   
* Implemented exhaustive hyper-parameter tuning of our Random Forest Regression model to arrive at the best performance, according to mean absolute error.  
* Developed a web application utilizing [Streamlit](https://streamlit.io) to allow for users to input values for our independent variables.  The web app then utilizes the serialized Random Forest Regression model to make predicts on the user inputted data.

## Demo of Web Application
You can of course interact with the Web Application yourself [here](https://share.streamlit.io/yiannimercer/career_salary_estimator/main/app.py)!
![Demo](https://github.com/yiannimercer/career_salary_estimator/blob/main/streamlit-app-2021-11-20-14-11-08.gif)

## Code and Resources Used
* See requirements.txt for a list of Python libraries that were utilized
* [Initial Glassdoor Web Scraper](https://github.com/arapfaik/scraping-glassdoor-selenium) (Script was edited due to the HTML code of Glassdoor being updated since this repository was finalized)
* [Initial Project Inspiration](https://www.youtube.com/watch?v=MpF9HENQjDo&list=RDCMUCiT9RITQ9PW6BhXK0y2jaeg&index=3) (Scarping Data Scientist Job Postings)
* [Deploying a Model Using Pickle and Streamlit](https://www.analyticsvidhya.com/blog/2020/12/deploying-machine-learning-models-using-streamlit-an-introductory-guide-to-model-deployment/)

## Data Collection, Cleaning & Feature Engineering
After updating the web scraper that was previously developed to the most recent (Nov, 2021) HTML Code that Glassdoor is using, the following variables were collected for each job posting:

* **Job Title** - Title of the Job Posting on Glassdoor (E.g., Senior Data Scientist, Junior Dental Hygienist)
* **Salary Estimate** - The Glassdoor provided average salary estimate based on previous employees in the same company and/or position who have reported their earnings to the platform.  (E.g., Employer Provided Salary: $80K - $100K)
* **Job Description** - A brief description of the job, responsibilities, and other need to know's that the company has chosen to share.
* **Company Rating** - A float data type representing the company's average rating, on a scale from 1.0 to 5.0 (E.g., 3.7)
* **Company Name** - The name of the company who is offering the job (E.g., Amazon.com Services LLC)
* **Location** - The location of where the job is being offered (E.g., Sandy, TX)
* **Size** - The size of the company as a whole. (E.g., 10000+ Employees)
* **Founded** - The year the company was founded (E.g., 1994)
* **Type of Ownership** - A string variable indicating if the company is public, private, school/university, government, etc. (E.g., Company - Public)
* **Industry** - The industry the company is in (E.g., Internet)
* **Sector** - The sector the company is in (E.g., Information Technology)
* **Revenue** - The revenue the company earns each fiscal year (E.g., $10+ Billion)

Additionally, various features were engineered or appended to the data frame that was developed.  Below is a list of these features.  

* **Simplified Job Title** - The name of the career that was searched in Glassdoor (E.g., Data Scientist, Data Hygienist, IT Manager)
* **Hourly** - Indicator column to show if the Estimated Pay is an hourly rate (1 = Hourly Pay Rate | 0 = Annually)
* **Employer Provided** - Indicator column to show if the Estimated Pay was provided by the employer (1 = Employer Provided | 0 = Glassdoor Average Values of similar roles)
* **Min Salary** - The minimum value of the range that is contained in the *Salary Estimate* variable
* **Max Salary** - The maximum value of the range that is contained in the *Salary Estimate* variable
* **Average Salary** - The computed average of the *Min* and *Max Salary* variables (if the salary provided was not a *range*, but a single value, both the *Min* and *Max Salary* features would be equal, so the *Average Salary* would be equal to the original *Salary Estimate*).  **If the hourly indicator was *True*, then the *Min* and *Max Salary* variables were converted to annual rates by multiplying the hourly pay by 2000.**
* **Company Text** - The result company name after various string cleaning techniques were made use of (E.g., removing extra characters, or numbers that were incidentily parsed as the *Company Name*)
* **Job State** - The state the job is being offered in (I.e., the state portion of the *Location* variable)
* **Age** - The age of the company (I.e., 2021 - Founded)
* **Seniority** - A string variable that indicates the level of seniority the position being offered is (E.g., *Junior*, *Senior*, *nan*)

## Exploratory Data Analysis (With Minor Data Touch Up)

The [Exploratory Data Analysis Notebook](https://github.com/yiannimercer/career_salary_estimator/blob/main/exploratory_data_analysis.ipynb) features various data analysis methods used to understand our data.  Prior to the analysis however, some previously lapsed data errors or missed items were addressed.  For example, the *job_state* variable did not have the correct format, or cities in place of the state.  Additionally, we removed rows where numeric columns are null or were not valid at this point.  We also converted our respective features to their appropriate data types (i.e., int, object, etc.). Various bar, box, distribution, and correlation plots, along with group by aggregated tables were utilized to gain insights into our dataset.  Below are some highlights of the analysis.

#### Summary Statistics
![Summary Statistics](https://github.com/yiannimercer/career_salary_estimator/blob/main/Summary_stats.png)
#### Correlation Plot of Pure Numerical Variables
![Corr Plot](https://github.com/yiannimercer/career_salary_estimator/blob/main/corr_plot_num_variables.png)
#### Seniority Bar Plot
![Seniority Plot](https://github.com/yiannimercer/career_salary_estimator/blob/main/seniority_img.png)
#### Location Bar Plot (Sorted)
![Location Plot](https://github.com/yiannimercer/career_salary_estimator/blob/main/location_img.png)
#### Average Salary by Company Rating
Rating |Average Salary|
--- | --- |
1.0 | 157,226.496 |
2.0 | 102,184.138 |
3.0 | 99,387.576 |
4.0 | 102,718.746 |
5.0 | 134,175.620 |
-1 Not Found | 118,613.914 |
#### Average Salary by Hourly vs. Annual
Rating |Average Salary|
--- | --- |
1 (Hourly) | 127,210.297 |
0 (Annual) | 54,091.067 |
#### Average Salary by the Type of Ownership of the Company
Type of Ownership of the Company |Average Salary|
--- | --- |
Private Practice / Firm         |148.811052|
Company - Private               |114.325092|
Contract                        |107.555172|
Company - Public                |107.351118|
College / University            |105.716396|
Government                      |105.674370|
Subsidiary or Business Segment  |102.095779|
Hospital                        | 99.907876|
School / School District        | 87.400000|
Nonprofit Organization          | 82.521432|
Self-employed                   | 77.071942|
Franchise                       | 54.804124|
Unknown                         |125.805687|
-1 (Not Found)                  |116.426477|

## Model Building & Optimization
Knowing the problem called for a regression model, we opted for the following choices of algorithms.  The choices were based on the ability to progressively tune the hyper-parameters for performance and efficiency, relating to our scoring methods, and the run time of the model.  

1. Linear Regression
2. LASSO Regression
3. Random Forest regression

Linear Regression was chosen as a baseline, knowing we would not receive the most promising results, however to get an idea of the model building process and to kickstart our efforts we chose to utilize this algorithm.  We performed 3-fold cross validation, scoring the model based on the negative mean absolute error, and calculated the mean of these models.

Furthermore, we transitioned into fitting a LASSO regression model, which can be thought of a modified version of linear regression.  In LASSO, the loss function is modified to minimize the complexity of the model by limiting the sum of the absolute values of the model coefficients. [[1]](https://www.pluralsight.com/guides/linear-lasso-ridge-regression-scikit-learn)  We additionally chose to fit the LASSO model due to the sparse data from the many categorical variables, therefore a normalized regression like LASSO may be effective.  As an effort to substantiate our model through many iterations, we chose to fit and use a 3-fold cross validation, over 100 different values for alpha (*range(1,100) / 100*) ,  

Finally, a Random Forest Regression model was fit, again choosing this model due to many categorical variables, but also with the intention of further iterating through parameters the Random Forest Regressor allows, via [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html).  Initially, we fit the model using 3-fold cross validation, and scoring each iteration by its negative mean absolute error.  This model alone returned the most favorable results compared to the former two models, however as we mentioned, tuning of the hyper-parameters to optimize and arrive at the best model via GridSearch CV was performed.

## Findings & Model Performance

#### Linear Regression

Linear Regression by far performed the worst compared to any version of any model.  

Data Set | Mean Absolute Error |
--- | --- |
3-Fold Cross Validation on Training Set     |5204564.249911354|
Test Set                  |43907.414817765246|

#### LASSO Regression

LASSO Regression was much more promising than the previous Linear Regression Model.  By iterating through 100 values that would be multiplied against the L1 term, otherwise known as the *alpha* parameter, we were able to visualize the model as it progress through each.  While this plot (below) is rather basic, it paints a picture of increasing the *alpha* parameter, will only lead to a worse negative mean absolute error.  

![LASSO Error Plot](https://github.com/yiannimercer/career_salary_estimator/blob/main/lasso_alpha_plot.png)

Data Set | Mean Absolute Error |
--- | --- |
3-Fold Cross Validation on Training Set (Alpha = 0.01)     |19.236062|
Test Set                  |18.334629248453158|

#### Random Forest Regression

Random Forest, before any tuning of the hyper-parameters, still outperformed both of our previous models.  Like the formers, we also applied 3-Fold Cross Validation, scoring based off the negative mean absolute value.  Calculating the mean of these models, **we arrived at mean absolute value of 17.258649699296782.**  

However, we wished to optimize the Random Forest Regressor Model even further by performing Sklearn's model selection class, GridSearchCV.  The following instances of the Random Forest's parameters were declared in the dictionary below:

*parameters = {'n_estimators':range(10,300,60), 'criterion':['mse'], 'max_features':('auto','sqrt')}*

The parameter dictionary was then passed to the GridSearchCV function, indicating a 3-Fold Cross Validation also be performed for each combination of parameter values.  After generating predictions on our test set, **the calculated mean absolute error of 16.42386175902106** easily indicated our arrival at our best performing model.  

## Deploying Model to Web Application

#### Pickle

Utilizing the Python module, *Pickle* we serialized the final Hyper-Parameter Tuned Random Forest Regression model by saving the model object and passing it into the *dump* function of *Pickle*.  This will not only serialize the object, but also convert it into *byte-stream* that we can save as a file called, *regressor.pkl*.

      import pickle
      pickle_out = open("regressor.pkl", mode = "wb")
      pickle.dump(gs.best_estimator_, pickle_out)
      pickle_out.close()


#### Streamlit
