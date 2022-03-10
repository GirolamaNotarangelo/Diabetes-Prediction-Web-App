# Diabetes-prediction-model

## CONTEXT
Diabetes is a chronic (long-lasting) health condition that causes a person's blood sugar level to become too high. 
With a relatively long asymptomatic phase, early intervention is very important in stopping the progression and damages of Diabetes. The early diagnosis of diabetes is only possible by proper assessment of certain factors and symptoms.

## AIM
With this project I want to build a model that predict if a patient is at risk to be diagnosed to have diabetes or not based on a list of some factors and early symptoms. I then built a web app to deploy my model using Flask and Heroku. You can check the web app here https://predict-diab.herokuapp.com/

## DATASET

The dataset has been downloaded from  [UCI Machine Learning Repository ](https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.#) and it is has been collected in 2020 using direct questionnaires of 520 patients of Sylhet Diabetes Hospital in Sylhet, Bangladesh and approved by a doctor.

## FILES
- Diabetes prediction model.ipynb : Jupyter Notebook with Exploratory Data Analysis (EDA) using Pandas and NumPy and trained models.
- app.py : Web App script
- index.htlm: html code for the Web App
- requirements.txt : pre-requiste libraries for the project
- diabetes_data_upoload: dataset 
- 


## Techniques/Models
- Oversampling Technique (SMOTE)
- Linear Regression model
- Random Forest
- Gradient Boosting
- Cross validation for each algorithm

The project was developed using Python 3.8.3 with the following packages.

- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-learn
- Imblearn
- Pickle

## Further improvements
- It would be useful to work with a bigger dataset in order to improve the predictive model.
- Would be nice to create a better looking  web-app. An idea could be the use of  Streamlit.
- Working on understanding and evaluating which combinations of symptoms and factors give higher percentage of positive prediction.
- Working on understanding and evaluating which combinations of symptoms and factors give higher percentage of positive prediction.

