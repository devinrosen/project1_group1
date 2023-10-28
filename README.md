# Residential Real Estate vs Supply, Inflation, and Interest Rate

## Description
Our goal is to determine how the value of residential real estate relates to supply, inflation, and interest rate.  Based on these economic factors, can we discern optimal periods for buying or selling residential real estate for investment purposes.  Additionally, we will explore how real estate compares to equities by measuring residential real estate values to the S&P 500 and XLRE (Real Estate Select Sector).

## Objectives
 - We intend to identify ideal periods to transact residential real estate based on supply, inflation, and interest rate.
 - We intend to compare residential real estate returns to the S&P 500 and XLRE for investment purposes.

## Requirements
 - [fredapi](https://github.com/mortada/fredapi)
    - To install fredapi: `pip install fredapi`
    - Create an account at [Fred](https://fred.stlouisfed.org/)
    - Create a [Fred api key](https://fredaccount.stlouisfed.org/apikeys)
    - Add the Fred api key to your .env with the format `FRED_API_KEY={fred_api_key}`
 - [yfinance](https://github.com/ranaroussi/yfinance)
    - To install yfinance: `pip install yfinance`

## Residential Real Estate Value Compared to Inflation
In this section, we are conducting a comparison between the Housing Price Index and inflation. Over time, a noticeable similarity emerges as both the Housing Price Index and inflation follow a parallel trend until the year 2010.
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Inflation%20and%20HPI.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Inflation%20and%20HPI%20Analysis.png?raw=ture)

## Residential Real Estate Value Compared to Federal Funds Effective Rate
In this particular scenario, we are examining the relationship between the Housing Price Index and interest rates. During the initial years, as interest rates were on the rise, the Housing Price Index remained relatively stable with minimal fluctuations. However, post-2001, a notable trend emerges wherein the Housing Price Index undergoes significant fluctuations over time.
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Interest%20Rate%20and%20HPI.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Interest%20Rate%20and%20HPI%20Analysis.png?raw=true)


## Residential Real Estate Value compared to Monthly Supply of New Houses
Regarding the supply of new houses and the Housing Price Index, we observe that the monthly supply of new houses has consistently exceeded the Housing Price Index. However, in the period following 2000, the Housing Price Index has shown variations while the monthly supply of new houses has maintained a steadier pace.

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Monthly%20Supply%20New%20House%20and%20HPI.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/House%20Monthly%20Supply%20and%20HPI%20Analysis.png?raw=true)


## Combined Residential Real Estate Value, Inflation, Fred Funds Effective Rate, Monthly Supply of New Houses
In this analysis, we are examining the Housing Price Index, Interest Rate, and monthly supply of new houses. From the graphical data, a notable pattern emerges. In 1981, during a period of high Interest rates, we observe low inflation, a corresponding low Housing Price Index, and a rising monthly supply of new houses. Conversely, in 2010, when Interest rates were low, we see the highest monthly supply of new houses, low inflation, and a declining Housing Price Index.
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Combined%20Dataframe.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Correlation.png?raw=true)

##### Correlation Analysis
*	HPI and inflation show a positive correlation, indicating that an increase in HPI is associated with an increase in inflation.
*	Monthly supply and interest rate display a positive correlation, meaning that when monthly supply increases, Interest rates also tend to increase.
*	Monthly supply and inflation demonstrate a negative correlation, explaining that an increase in monthly supply is associated to a decrease in inflation.
*	Monthly supply and HPI show a negative correlation, suggesting that as monthly supply increases, HPI tends to decrease.
*	Interest rate and inflation reveal a negative correlation, indicating that an increase in interest rate is linked to a decrease in inflation.
*	Interest rate and HPI have a negative correlation, indicating that when interest rates increase, HPI tends to decrease.


##### How do cycles in Inflation, Interest rates and housing inventories affect the costs of residential real estate since 1980?
In 1980, as interest rates were on the rise, they had a marginal positive effect on the Housing Price Index, inflation, and monthly supply. However, in 1981, when Interest rates reached their peak, a negative impact was observed on inflation and the Housing Price Index, although monthly supply continued to increase at a slower rate. Fast forward to 2010, with Interest rates at their lowest, monthly supply reached its peak, while both the Housing Price Index and inflation experienced a decline.


## Residential Real Estate Value Compared to Economic Factors



# PART 2 - Investment Analysis: Housing Price Index(HPI) vs S&P 500 vs The Real Estate Select Sector SPDR Fund (XLRE)

## a.Residential Real Estate Returns Compared to S&P 500
We started the investment analysis by importing the yfinance (Yahoo Finance), python library to pull in historical data. The yfinance tool only pulled in data back to 1985 and for that reason we narrowed our investment scope for the HPI to go back to only the start of 1985 as well. Secondly, since the HPI is a quarterly report we pulled in quarterly S&P 500 data, rather than daily or monthly records. Once we had our time and frequency variables in equilibrium we focused on the closing data for both the S&P 500 and HPI and then calculated and plotted the returns for HPI and S&P both individually and against each other.
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/S&P500_Quarterly_Returns.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/HPI_Quarterly_Returns.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/S&P500_and_HPI_Returns.png?raw=true)

#### Analysis Results

## b.Residential Real Estate Returns Compared to XLRE
We then pivoted to compare the HPI to the he Real Estate Select Sector SPDR Fund (XLRE). The XLRE fund is a fund that was created towards the end 0f 2015 with their first quarterly report being 10/1/2015. This fund is a cumulation of securities of companies in the real estate industry, real estate management and development companies and REIT's. For this comparison we re-sliced the HPI data to also start with first data entry being that of 10/01/2015. We then repeated the process from the analysis above by fetching the quarterly closing dates for both HPI and XLRE and calculated and plotted returns for each asset individually and against each other.

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/XLRE_Quarterly_Reports.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/XLRE_HPI_Returns.png?raw=true)


## c.Residential Real Estate Returns Compared to XLRE & S&P500
Lastly, we then re-sliced the S&P 500 data to also have a data starting point of 10/01/2015. After combining all 3 asset class returns into a single data frame we were able to plot all 3 against each other for an easy-viewing, investment analysis of returns between the 3 assets. 
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/XLRE_HPI_SP500_Returns.png?raw=true)




#### Analysis Results