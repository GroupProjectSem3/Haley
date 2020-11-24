# HALEY :dancer: 
[![GitHub issues](https://img.shields.io/github/issues/GroupProjectSem3/Haley)](https://github.com/GroupProjectSem3/Haley/issues)
[![GitHub forks](https://img.shields.io/github/forks/GroupProjectSem3/Haley)](https://github.com/GroupProjectSem3/Haley/network)
[![GitHub stars](https://img.shields.io/github/stars/GroupProjectSem3/Haley)](https://github.com/GroupProjectSem3/Haley/stargazers)
[![Python Version](https://img.shields.io/badge/Python-3.5|3.6-blue.svg)](https://shields.io/)
[![GitHub license](https://img.shields.io/github/license/GroupProjectSem3/Haley)](https://github.com/GroupProjectSem3/Haley/blob/master/LICENSE)
![Python Syntax](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/workflows/Python%20Syntax/badge.svg)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

![IMAGE ALT TEXT HERE](https://github.com/GroupProjectSem3/Haley/blob/master/images/Haley.png)

## Table of Contents
- [What it Does](#what-it-does)
- [How it Works](#how-it-works)
- [Requirements](#requirements)
  * [Hardware](#hardware)
  * [Software](#software)
- [Setup](#setup)
  * [Run the application](#run-the-application)
- [Data Source](#data-source)
- [Test Cases](#test-cases)


## What it Does
>‘Haley’ is a one-stop destination for an individual’s complete health monitoring that tracks the most common symptoms in its core. We are designing and implementing a web application which enables a user to record their medical history. Through this platform, we will ask users questions & based on their response, we give them predictions about what ails them. The idea is to develop a reliable and accessible platform that gives user-health advice such that they can avail home remedies and over the counter solutions if the waiting period for GP appointment is long.

>Additionally, the users will be given a list of General Practitioners based on their location from whom they can get a professional opinion. ‘Haley’ is a health monitoring application that keeps a track of common symptoms to contain the future outbreak by making citizens aware of the impact based on data and sound reasoning such that we can send out an alarm if a lot of people report the same issue in a period of time. Given we aim to make the app accessible to all kinds of user groups; we aim the app to reach everyone.

## How it Works
The minimum viable product for this project will be a working web application which allows the users to-
*	Login/Register on the app
*	Track their previous medical history
*	Check their new symptoms and get a diagnosis.
*	Get few home remedies to manage the symptoms as suggested by HSE/WHO.
*	Get a list of GPs near their location which they can consult.


## Requirements

### Software
1. django >=1.9, <2
2. applicationinsights

### Hardware
To be announced


## Setup

### Run the application 
* Create virtual environment: virtualenv venv -p python
* Activate the environment: .\venv\Scripts\activate
* Install all requirements: pip install -r requirements.txt
* Migrate all changes to Database: python manage.py migrate
* Run the server: python manage.py runserver
  (Server runs at http://127.0.0.1:8000/)


## Data Source
The Dataset we will use for this project is obtained by using the combine approach of finding existing datasets and generating new ones. We are getting data from open source repository like Kaggle, GitHub, UCI and Google datasets as well as using real time experience from doctors to synthesize a dataset using java code. The java code ensures the elimination of conscious bias from the dataset. The final dataset contains 101 columns and 250001 rows amounting to 490001 data points. 
* [Kaggle diseases dataset](https://www.kaggle.com/priya1207/diseases-dataset)
* [Kaggle questionnaire dataset](https://www.kaggle.com/moradnejad/nhanes-questionnaires-datasets-20172018-csv?)
* [Kaggle heart diseases dataset](https://www.kaggle.com/johnsmith88/heart-disease-dataset)
* [Kaggle Chronic Kidney diseases dataset](https://www.kaggle.com/mansoordaku/ckdisease)
* [GitHub Medical dataset](https://github.com/adalca/medical-datasets)
* NHS, WHO and HSE website
* Qualified doctors (with more than 10 years of work experience) help.


## Test Cases
Develop test cases to review work such as
* Frontend - page navigation working properly,
* Backend - Able to fetch and insert data into tables, and
* Model - library call is successful

can be found [here](https://drive.google.com/file/d/1eb_F5XE5R0ldAp-P0bCLveQUhN8HD6Jb/view?usp=sharing)
