# This repository contains my submissions for the IBM Data Science Professional Certificate capstone project.

# The overall objectives of the capstone project were to collect data about SpaceX Falcon 9 rocket launches from public sources and build a Machine Learning pipeline to predict launch success. 

# This repository includes multiple Jupyter notebooks showing the specific objectives for various elements of the capstone project and my Python code leveraging various libraries/packages such as Pandas, Numpy, SKLearn, Plotly, etc. to meet these objectives. 

# The project involved the following sequential steps:

#   1. Collect data from the SpaceX API; parse the data and create a Pandas dataframe - use requests and helper functions to get data, normalize the json, create the dataframe and handle missing values

#   2. Collect data (using web scraping) from Wikipedia about SpaceX Falcon 9 launches and create a Pandas dataframe - use requests, Beautiful Soup and helper functions to get the data, parse the HTML data and create the dataframe

#   3. Data wrangling to get a basic understanding of the data and to create the training label (Launch Success/Failure) - use Pandas & Numpy to understand the available data

#   4. Exploratory Data Analysis using SQL and data visualization - use SQL Alchemy & Seaborn to deepen understanding by examining relationships between various data elements and performing feature engineering to prepare for the modeling phase

#   5. Interactive Visual Analysis & Dashboard Development - use Folium, Plotly & Dash to enable direct data exploration, identify patterns more effectively and prepare the data for effective story telling

#   6. Construct a Machine Learning Pipeline to predict launch success - use SciKit Learn to preprocess the data, split the dataset into training & testing samples, develop multiple models and optimize them using hyperparameters

#      Specific SKLearn components used include: 
#        a) preprocessing (StandardScaler) to standardize the data
#        b) train_test_split to create and appropriately stratify the training and testing datasets
#        c) 4 specific modeling techniques - Logistic Regression, Support Vector Machines (SVM), Decision Tree Classifier and K-Nearest Neighbors (KNN)
#        d) GridSearchCV to test various hyperparameters to optimize the models
#        e) metrics (Confusion Matrix, accuracy, precision, etc.) to evaluate the various models and identify the best model
