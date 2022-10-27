# Final-Project_Bass_Fishing_Analysis

# Segment 1 Overview
mlf logo
## The data set I have chosen is from Major League Fishing a professional fishing organization that has tournaments in a catch-weigh-release style. I'm an avid fisherman myself and I thought it would be a great data source for somthing I'm intrested in. The data source is stored on the MLF website and will need to be screen scraped.
fishing data example
## The data contains 8 useful columns of data Angler, Species, Weight, Bait, Area, Cover, Depth, and Recorded time of catch.
## The main question I want to answer is can I build a model that uses the controllable features (Bait, Area, Cover, Depth, and time) to predict the weight of a fish caught.
## A useful question along the way to answer is do any of the features contribute more to the target(weight)

# Github
## I have this readme file!
## Communication is easy since its just myself working on the project
## I currently have 6 branches and have made several commits to each of them.
github branches pic

# Screen Scrape
## I wrote a screen scraper that will login to the MLF web page and click on each angler then copy the data to a pandas dataframe. Currently the screen scrape saves to a csv and I manually import into the database but I plan to update so that it pulls in directly.
web scrape picture

# Data Cleaning
## Some of the data is in formats that I would like to change. The fish weight is in a lbs-oz format and needs to be in a continuous format (lbs)
## Also changed the time to a 24 hour format
## the data cleaning pulls from database and stores the cleaned data into a new table on the database.
data cleaning picture

# Database
## I created a PGAdmin Postgresql database called Fish_Catch_Data
## I currently have 2 tables in it one to store the screen scrape
pic of screen scrape data in pgadmin
## And another for the cleaned data

# ML Model
## Currently I have a keras model structure that pulls the cleaned data in from the database.
## I used binning to shrink the amount of data point within some of the more complex columns and then used the hot encoder to prepare the data for the model.
pic of binning and dropping
pic of keras model
