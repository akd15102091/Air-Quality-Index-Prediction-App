# Air-Quality-Index-Prediction

This application tell us about **Air Quality Index (for Banglore)** .

The App Link :    https://air-quality-prediction-app.herokuapp.com/

Application Video link :   https://drive.google.com/file/d/1GbqpEYI8DmfFlNUqT9WRLn6VqMbsZWHj/view?usp=sharing

Some Glimpses of Application : 

![rcd1](https://user-images.githubusercontent.com/61588604/108498811-6e5a2700-72d3-11eb-81df-f95e1a836af9.png)

![rcd2](https://user-images.githubusercontent.com/61588604/108498891-803bca00-72d3-11eb-8780-4ceb8b297f71.png)

![rcd3](https://user-images.githubusercontent.com/61588604/108498928-8df14f80-72d3-11eb-8a8d-6afbd6f23af7.png)


Journey : 

**1) Data Collection** :  Data collecting process of thus project is AWESOME .

    a) used third party api and using python , "retrieve data of every day of every month of 2013-2018 year" from the html pages( web pages) of the BANGLORE Place .
    b)about data : Data Columns are : Average Temperature(T), Maximum Temperatre(TM), Minimum Temperature(Tm), Atmospheric Pressure at sea level (SLP), Average Relative Humidity(H) , Average Visibility, Average wind speed(V), Maximum sustained wind speed(VM), AQI-index ( PM 2.5 ) . 
    
    c) As a data scientist, we will predict the Air-Quality-Index for Banglore place, if user enter some features values as input .
    
    
**2) Data Preprocessing :** 
        
        a) checked the null values and removed those . 
        
        b) we collected data from 3rd party api using python so there were not many null values. All data is numerical .
        
        c) checked data that it is in guassian form. then scaled the data for some models (like linear , lasso, ridge...) because ensemble machine learning model don't need the scaled data .
        
        d) Now we can build machine learning models .
        
        

    
**3) Model building** : 

    a) split the dataset into X(independent features) and y(dependent features) .
    
    b) perform train_test_split .
    
    c) buoid models of -  linear regression,Lasso Regressor,Ridge regression , DecisionTreeRegressor, KNearestRegressor, RandomForestRegressor with hyperparameter tuning, XgBoost with hyperparameter tuning. 
    
    d) obsered that XGBoostRegressor with some parameters(got from hyperparameter tuning) has highest score and lowest error . so save this XgboostRegressor model using pickle.

**4) Model deployment** : 

    a) using flask framework , we deployed this model on HEROKU platform .
    
App link :  https://air-quality-prediction-app.herokuapp.com/
    
    

