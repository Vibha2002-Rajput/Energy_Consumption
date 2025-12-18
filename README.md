# Energy Consumption Forecasting Using Machine Learning

Energy consumption is on the increase and has a significant impact on the environment. Current predictions show that the growing trend of CO2 emissions which is often held responsible for most of the Earth’s progressive warming will continue therefore, international political, economic, and environmental research has focused on energy consumption reduction and energy efficiency improvement to cope with the problem of global warming and over-exploitation of natural resources.

Forecasting electricity demand and consumption accurately is critical to the optimal and cost effective operation system, providing a competitive advantage to companies. In working with seasonal data and external variables, the traditional time-series forecasting methods cannot be applied to electricity consumption data. In energy planning for a generating company, accurate power forecasting for the electrical consumption prediction, as a technique, to understand and predict the market electricity demand is of paramount importance.

Their power production can be adjusted accordingly in a deregulated market. As data type is seasonal, Seasonal Autoregressive Integrated Moving Averages with exogenous repressors (SARIMAX), and Decision Tree, Random forest is used to explicitly deal with seasonality as a class of time-series forecasting models.

The main purpose of this project is to perform exploratory data analysis of the Spain power, then use different forecasting models to once-daily predict the next 24 hours of energy demand and daily peak demand. To split the electricity consumption data into training and test sets. The obtained results showed that the machine learning algorithms proposed in the recent literature outperformed the tested algorithms. Models are evaluated using root mean squared error (RMSE) to be directly comparable to energy readings in the data. RMSE has calculated two ways. First to represent the error of predicting each hour at a time. Second to represent the models’ overall performance. The results show that electricity demand can be modeled using machine learning algorithms, deploying renewable energy, planning for high/low load days, and reducing wastage from polluting on reserve standby generation, detecting abnormalities in consumption trends, and quantifying energy and cost-saving measures.

## Objectives and Scope of the project

The aim of this project is to test whether a general and simple approach based on Machine Learning models, can yield good enough results in a complex forecasting problem, exploring machine learning techniques and developing data-driven models for forecasting energy consumption and performance. The fundamental objective of this project is to compare different Machine Learning models on the forecast mission of electricity load by using past data and evaluate the models’ performance.

This aim was broken down into as follows:
1. Implement classical statistical forecasting models
2. Implement and gain insight into walk forward validation, forecasting performance, and feature selection

## Details of Software and hardware Requirements
1. Hardware Requirement:
- Minimum space required is 500GB.
- RAM required is 8GB.
- Minimum space required in HDD is 1 TB and in SSD is 128 GB.
- Internet Connection
- Windows 7, 8.1 or any higher version

2. Software requirements:
- Windows 7, 8.1 or any higher version
- Python 3 or any higher version
- Packages required:
- NumPy
- Matplotlib
- Pandas
- Scikit Learn
- Seaborn
- PyMySQL
- Tkinter

## Data Collection

In this section we are going to elaborate the dataset which is used in this project to train the Machine learning model. The dataset we have used for this project is in the structured format. The dataset which is being used contains all the name of energy. Since this system based on supervised Machine learning algorithm, the dataset is labeled in GWh. After this, we have divided the dataset into two phases i.e training datasets and testing datasets. We trained our models using Machine learning algorithms to this training datasets to get trained Machine learning model. At last we provided the training datasets to this trained model to test the accuracy of model

[Monthly Electricity Consumption.csv](https://github.com/Vibha2002-Rajput/Energy_Consumption/files/11506309/Monthly.Electricity.Consumption.csv)

## Process for Forecasting Energy Consumption

![Process for Forecasting Energy Consumption](https://github.com/Vibha2002-Rajput/Energy_Consumption/assets/87843420/021f4696-910a-4577-9a78-3b9997265eb1)

## Conclusion:
In this project, the monthly electricity load consumption is used to forecast future load electricity demands. As such, traditional techniques may not be able to forecast future values accurately. The monthly electricity load values between 01/01/2018 to 30/06/2022, are reported in World energy dataset. In chapter 1, we summarized the importance of demand forecasting and related literature. To explore the dataset’s characteristics, we started with exploratory data analysis, providing descriptive information. In the data cleaning process, we will replace null values with mean values, extracted redundant attributes, and aggregated monthly load values monthly level to see the trend and seasonality functions more clearly.

# Research Paper of Energy Consumption Forecasting Using Machine Learning

Energy Consumption Forecasting using Machine Learning International Journal of Innovative Research in Technology 

https://ijirt.org › master › IJIRT158582_PAPER

[Research Paper](https://ijirt.org/master/publishedpaper/IJIRT158582_PAPER.pdf)

