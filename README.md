# Car Price Predictor App - Regression Analysis

## Table of Content
* [Demo](#demo)
* [Abstract](#abs)
* [Motivation](#motivation)
* [About the Data](#data)
* [Feature Engineering And Modeling](#model) 
  * [The Math Behind the Metrics Used](#metrics)
  * [Why I used Polynomial Features?](#poly)
  * [Why I converted my data into log normal distribution?](#log)
  * [Why I perform One Hot Encoding on my data?](#ohe)
  * [Why I did feature scaling?](#fs)
  * [Training With Linear Models?](#linear_models)
  * [How I found the best model and their best parameters using sklearn Pipelines and GridSearchCV?](#best_model)
* [Credits](#credits)

## Demo <a id='demo'></a>
The final Output for the project can be viewed [here](https://car-price-predictor-1.herokuapp.com/)

![Demo](https://raw.githubusercontent.com/animesharma3/Car-Price-Predictor---Regression-Analysis/master/demo.png)

## Abstract <a id='abs'></a>
* [Car Price Predictor](https://car-price-predictor-1.herokuapp.com/) is an **end-to-end Machine Learning Regression project**, built using **Flask** and deployed on **Heroku Cloud Platform**, which will help an **individual/dealer** to **predict the price** they can expect for any of their old car they would like to sell. The **dataset** on which the **ML models** are trained is taken from **kaggle**, provided by **cardekho.com**, has 4341 records and 8 dependent features.
* Various **ML models** are **tuned and trained** by making use of **sklearn pipelines and GridSearchCV**. Various **linear models, tree models and ensemble techniques** are employed for training (with all possible hyperparameters properly tuned). Out of them **Lasso(alpha=0.01)** happens to have better **r2-score** and least **Root Mean Squared Error.**

## Motivation <a id='motivation'></a>
My motivation for this project came from the **#66daysofdata** initiative started by **Ken Jee** from Youtube. If I haven't partipicated in this initiative, I may not be as accountable and consistent as I am in learning Data Science today.

## About the Data <a id='data'></a>

## Feature Engineering and Modeling <a id='model'></a>
* ### **The Math behind the metrices used**<a id='metrics'></a>
  * #### R2 Score
  <img src='https://miro.medium.com/max/2812/1*_HbrAW-tMRBli6ASD5Bttw.png' width="300">
 
  * #### Mean Squared Error
  <img src='https://cdn-media-1.freecodecamp.org/images/hmZydSW9YegiMVPWq2JBpOpai3CejzQpGkNG' width='300'>

* ### **Why I used Polynomial Features?**<a id='poly'></a>
  * Earlier for almost all the models, **r2_score** is close to **0.73**
  * But after increasing the no. of independent features to 45 using **sklearn.preprocessing.PolynomialFeatures** of **degree 2** the **r2_score** increases to **0.94** i.e
**Our Model is fitting better**, which is evident from the graphs below, which is basically plotted to show the **variance** between the actual and predicted value of Selling Price
<br>

   
                   Before Applying Polynomial Features            |            After Applying Polynomial Features
  <img src='https://github.com/animesharma3/Car-Price-Predictor---Regression-Analysis/blob/master/images/download.png' width='450' class='img' style='display:inline'>     <img src='https://raw.githubusercontent.com/animesharma3/Car-Price-Predictor---Regression-Analysis/master/images/index.png' width='450' class='img'>
  
 * ### **Why I converted my data into log normal distribution?**<a id='log'></a>
   * One of the basic assumption when you are training a **Linear Regression** model or compiling an **Artificial Neural Network** is that your data is **normally distributed**. I plotted the graph, I got some bell curve but I was not sure whether it is perfectly normally distributed. So I performed the **log normal distribution** for all my numerical data.

* For more deep dive into the modelling stuff you can check out the [Ipython Notebook for Feature Engineering and Choosing Best Model](https://github.com/animesharma3/Car-Price-Predictor---Regression-Analysis/blob/master/Feature%20Engineering%20and%20Choosing%20Best%20Model.ipynb)

## Credits <a id='credits'></a>
Special thanks to 
* **cardekho.com** for providing the dataset
* **Google Colaboratory** for providing the computational power to build and train the models.
* **Heroku** for making the deployment of this project possible.
* **#66daysofdata** community created by **KenJee** that is keeping me accountable in my Data Science Journey.
