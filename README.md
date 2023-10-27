# Residential Real Estate vs Supply, Inflation, and Interest Rate

## Description
Our goal is to determine how the value of residential real estate relates to supply, inflation, and interest rate.  Based on these economic factors, can we discern optimal periods for buying or selling residential real estate for investment purposes.  Additionally, we will explore how real estate compares to equities by measuring residential real estate values to the S&P 500 and XLRE (Real Estate Select Sector).

## Objectives
 - We intend to identify ideal periods to transact residential real estate based on valuation, inflation, and interest rate.
 - We intend to compare residential real estate returns to the S&P 500 and XLRE for investment purposes.

## Requirements
 - New Python Dependencies
    - [fredapi](https://github.com/mortada/fredapi)
        - To install fredapi: `pip install fredapi`
        - Create an account at [Fred](https://fred.stlouisfed.org/)
        - Create a [Fred api key](https://fredaccount.stlouisfed.org/apikeys)
        - Add the Fred api key to your .env with the format `FRED_API_KEY={fred_api_key}`
    - [yfinance](https://github.com/ranaroussi/yfinance)
        - To install yfinance: `pip install yfinance`

## Residential Real Estate Value Compared to Inflation
In this section, we are comparing between Housing Price Index and Inflation. 
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Inflation%20and%20HPI.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Inflation%20and%20HPI%20Analysis.png?raw=ture)

## Residential Real Estate Value comapred to Federal Funds Effective Rate
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Interest%20Rate%20and%20HPI.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Interest%20Rate%20and%20HPI%20Analysis.png?raw=true)


## Residential Real Estate Value compared to Monthly Supply of New Houses

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Monthly%20Supply%20New%20House%20and%20HPI.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/House%20Monthly%20Supply%20and%20HPI%20Analysis.png?raw=true)


## Combined Residential Real Estate Value, Inflation, Fred Funds Effective Rate, Monthly Supply of New Houses

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Combined%20Dataframe.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Correlation.png?raw=true)
## Residential Real Estate Value Compared to Economic Factors

## Residential Real Estate Returns Compared to S&P 500 and XLRE
