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
In this section, we are conducting a comparison between the Housing Price Index and Inflation. Over time, a noticeable similarity emerges as both the Housing Price Index and Inflation follow a parallel trend until the year 2010.
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Inflation%20and%20HPI.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Inflation%20and%20HPI%20Analysis.png?raw=ture)

## Residential Real Estate Value comapred to Federal Funds Effective Rate
In this particular scenario, we are examining the relationship between the Housing Price Index and Interest rates. During the initial years, as Interest rates were on the rise, the Housing Price Index remained relatively stable with minimal fluctuations. However, post-2001, a notable trend emerges wherein the Housing Price Index undergoes significant fluctuations over time.
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Interest%20Rate%20and%20HPI.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Interest%20Rate%20and%20HPI%20Analysis.png?raw=true)


## Residential Real Estate Value compared to Monthly Supply of New Houses
Regarding the Supply of New Houses and the Housing Price Index, we observe that the Monthly supply of New Houses has consistently exceeded the Housing Price Index. However, in the period following 2000, the Housing Price Index has shown variations while the Monthly Supply of New Houses has maintained a steadier pace.

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Monthly%20Supply%20New%20House%20and%20HPI.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/House%20Monthly%20Supply%20and%20HPI%20Analysis.png?raw=true)


## Combined Residential Real Estate Value, Inflation, Fred Funds Effective Rate, Monthly Supply of New Houses
In this analysis, we are examining the Housing Price Index, Interest Rate, and Monthly Supply of New Houses. From the graphical data, a notable pattern emerges. In 1981, during a period of high Interest rates, we observe low Inflation, a corresponding low Housing Price Index, and a rising Monthly Supply of New Houses. Conversely, in 2010, when Interest rates were low, we see the highest Monthly Supply of New Houses, low Inflation, and a declining Housing Price Index.
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Combined%20Dataframe.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Correlation.png?raw=true)

### Correlation Analysis

According to the correlation heatmap graph:
•	HPI and Inflation show a positive correlation, indicating that an increase in HPI is associated with an increase in Inflation.
•	Monthly Supply and Interest rate display a positive correlation, meaning that when Monthly Supply increases, Interest rates also tend to increase.
•	Monthly Supply and Inflation demonstrate a negative correlation, explaining that an increase in Monthly Supply is associated to a decrease in Inflation.
•	Monthly Supply and HPI show a negative correlation, suggesting that as Monthly Supply increases, HPI tends to decrease.
•	Interest Rate and Inflation reveal a negative correlation, indicating that an increase in Interest Rate is linked to a decrease in Inflation.
•	Interest rate and HPI have a negative correlation, indicating that when Interest rates increase, HPI tends to decrease.

## Residential Real Estate Value Compared to Economic Factors

## Residential Real Estate Returns Compared to S&P 500 and XLRE
