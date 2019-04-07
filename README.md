### Date created
This readme file was created on:

* 7th April 2019 - Version 1.0

### Project Title
Bike Sharing Data Analysis Application

### Description
Bike Sharing Data Analysis application provides statistical data based on 3 separate country's data:

1. Chicago
2. New York City
3. Washington

One of the major key feature of this application is that it allows you to make filters by:

- Country Name
- Month
- Day of the Week

Users are given the option to display the top 5 most recent data. Upon displaying the 5 most recent data, user can subsequently request to display further 5 more data.

### Files used
Files used for this project:

- bikeshare.py *(Main python file containing functional code)*
- chicago.read_csv *(Chicago bike share data in a CSV format)*
- new_york_city.csv *(New York city bike share data in a CSV format)*
- washington.csv *(Washington bike share data in a CSV format)*
- README.md *(Informative text file containing information on the project)*

### Credits
Credits to:

- **Udacity**
  * Providing the base structure of the bike share code and bike share data
- **Stack Overflow**
  * Always being the helpful outlet to cross check error message or new Pandas and Numpy functions

### Bug Fixes
1. Bug Fix 07/04/2019
  * Had an issue with displaying raw data where if the user does not choose the options **[Any Country]/[All]/[All]**, the user would get a KeyError error message. This was caused by the fact that the raw data was displayed based on dictionary keys that were incremental from the value 1 onwards. If the values were random or mixed, the dictionary key would not be found due to the for loop basing on a 1...2...3 incremental from 0, causing the KeyError error message.
