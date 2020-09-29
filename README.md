# Car Price Predictor App - Regression Analysis

## Table of Content
* [Demo](#demo)
* [Abstract](#abs)
* [Motivation](#motivation)
* [About the Data](#data)
* [Modeling](#model) 
* [Credits](#credits)

## Demo <a id='demo'></a>
The final Output for the project can be viewed [here](https://car-price-predictor-1.herokuapp.com/)

![Demo](https://raw.githubusercontent.com/animesharma3/Car-Price-Predictor---Regression-Analysis/master/demo.png)

## Abstract <a id='abs'></a>
* [Car Price Predictor](https://car-price-predictor-1.herokuapp.com/) is an **end-to-end Machine Learning Regression project**, built using **Flask** and deployed on **Heroku Cloud Platform**, which will help an **individual/dealer** to **predict the price** they can expect for any of their old car they would like to sell. The **dataset** on which the **ML models** are trained is taken from **kaggle**, provided by **cardekho.com**, has 4341 records and 8 dependent features.
* Various **ML models** are **tuned and trained** by making use of **sklearn pipelines and GridSearchCV**. Various **linear models, tree models and ensemble techniques** are employed for training (with all possible hyperparameters properly tuned). Out of them **Lasso(alpha=0.01)** happens to have better r2-score and least Root Mean Squared Error.

## Motivation <a id='motivation'></a>
My motivation for this project came from the **#66daysofdata** initiative started by **Ken Jee** from Youtube. If I haven't partipicated in this initiative, I may not be as accountable and consistent as I am in learning Data Science today.

## About the Data <a id='data'></a>

## Modeling <a id='model'></a>
For more deep dive into the modelling stuff you can check out the [Ipython Notebook for Feature Engineering and Choosing Best Model](https://github.com/animesharma3/Car-Price-Predictor---Regression-Analysis/blob/master/Feature%20Engineering%20and%20Choosing%20Best%20Model.ipynb)

## Credits <a id='credits'></a>
Special thanks to 
* **cardekho.com** for providing the dataset
* **Google Colaboratory** for providing the computational power to build and train the models.
* **Heroku** for making the deployment of this project possible.
* **#66daysofdata** community created by **KenJee** that is keeping me accountable in my Data Science Journey.
