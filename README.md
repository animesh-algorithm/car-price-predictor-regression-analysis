# Car Price Predictor App - Regression Analysis

## Table of Content
* [Demo](#demo)
* [Abstract](#abs)
* [Motivation](#motivation)
* [About the Data](#data)
* [Feature Engineering And Modeling](#model) 
  * [The Math Behind the Metrics Used](#metrics)
  * [Why I used Polynomial Features?](#poly)
  * [Why I converted the numerical data into log normal distribution?](#log)
  * [Why I perform One Hot Encoding on the data?](#ohe)
  * [Why I did feature scaling?](#fs)
  * [Training With Linear Models.](#linear_models)
  * [How I found the best model and their best hyperparameters using sklearn Pipelines and GridSearchCV?](#best_model)
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

                   Before Applying Log Normal Dist.               |            After Applying Log Normal Dist.
  <img src='https://github.com/animesharma3/Car-Price-Predictor---Regression-Analysis/blob/master/images/index1.png' width='450' class='img' style='display:inline'>     <img src='https://github.com/animesharma3/Car-Price-Predictor---Regression-Analysis/blob/master/images/index2.png' width='450' class='img'>

 * ### **Why I perform One Hot Encoding on the data?**<a id='ohe'></a>
   * My Data have some categorical features like **Fuel Type, Seller Type and Transmission**, which doesn't make sense to any Machine Learning or Deep Learning Models. Hence they needed to be converted into numerical data and one way to do that is through **One Hot Encoding**, which I did using **pd.get_dummies** function.
 
 * ### **Why I did feature scaling?**<a id='fs'></a>
   * All of my features have different units, ex. kilometers, no. of years, rupees etc. So I scaled all of my features.
   * I tried both **MinMaxScaler()** and **StandardScaler()**, the latter one worked better.

 * ### **Training with linear models**<a id='linear_models'></a>
   * I trained my dataset with various linear models for ex. **Linear Regression, Lasso Regression, Ridge Regression and Bayesian Ridge Regression**.
   * To my surprise all models performed same way with nearly same value of **r2_score, Mean Absolute Error and Mean Squared Error**.
   
                      Linear Regression               |            Lasso Regression
   <img src='https://github.com/animesharma3/Car-Price-Predictor---Regression-Analysis/blob/master/images/index3.png' width='400' class='img' style='display:inline'>     <img src='https://github.com/animesharma3/Car-Price-Predictor---Regression-Analysis/blob/master/images/index4.png' width='400' class='img'>   
   
                      Ridge Regression                |             Bayesian Ridge Regression
   <img src='https://github.com/animesharma3/Car-Price-Predictor---Regression-Analysis/blob/master/images/index5.png' width='400' class='img' style='display:inline'>     <img src='https://github.com/animesharma3/Car-Price-Predictor---Regression-Analysis/blob/master/images/index6.png' width='400' class='img'>

 * ### **How I found the best model and their best hyperparameters using sklearn Pipelines and GridSearchCV?**<a id='best_model'></a>
   * I made use of **sklearn pipelines** to its best. I created multiple pipelines with respect to the model and their hyperparameters. 
   * Then I combined the power of **sklearn pipelines** and **GridSearchCV**, which trained all the models for me, with all the possible hyperparamerter and finally gave the **best model** which in our case happens to be **Lasso(alpha=0.01)**.
   * I **dumped** that model using **pickle** library and then **loaded** the model into the **Flask** app.
   * The best model gave the following scores - 
       * R2 Score  - 0.9442452908334493
       * Mean Absolute Error -  0.7422001552130918
       * Mean Squared Error -  1.2843423154102787
   * And the following graph for the **variance in Predicted and Actual Value of Selling Price**
   <img src='https://github.com/animesharma3/Car-Price-Predictor---Regression-Analysis/blob/master/images/index7.png' width='400' class='img' style='display:inline'> 


* For more deep dive into the modelling stuff you can check out the [Ipython Notebook for Feature Engineering and Choosing Best Model](https://github.com/animesharma3/Car-Price-Predictor---Regression-Analysis/blob/master/Feature%20Engineering%20and%20Choosing%20Best%20Model.ipynb)

## Credits <a id='credits'></a>
Special thanks to 
* **cardekho.com** for providing the dataset
* **Google Colaboratory** for providing the computational power to build and train the models.
* **Heroku** for making the deployment of this project possible.
* **#66daysofdata** community created by **KenJee** that is keeping me accountable in my Data Science Journey.
