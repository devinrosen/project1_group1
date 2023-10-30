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

##### Correlation Analysis
*	HPI and Inflation show a positive correlation, indicating that an increase in Inflation is associated with an increase in HPI and vice versa.
*	Monthly Supply and Interest rate display a positive correlation, meaning that when Monthly Supply increases, Interest rates also tend to increase.
*	Monthly Supply and Inflation demonstrate a negative correlation, explaining that an increase in Monthly Supply is associated to a decrease in Inflation.
*	Monthly Supply and HPI show a negative correlation, suggesting that as Monthly Supply increases, HPI tends to decrease.
*	Interest Rate and Inflation reveal a negative correlation, indicating that an increase in Interest Rate is linked to a decrease in Inflation.
*	Interest rate and HPI have a negative correlation, indicating that when Interest rates increase, HPI tends to decrease.


##### How do cycles in Inflation, Interest rates and housing inventories affect the costs of residential real estate since 1980?
In 1980, as Interest rates were on the rise, they had a marginal positive effect on the Housing Price Index, Inflation, and Monthly Supply. However, in 1981, when Interest rates reached their peak, a negative impact was observed on Inflation and the Housing Price Index, although Monthly Supply continued to increase at a slower rate. Fast forward to 2010, with Interest rates at their lowest, Monthly Supply reached its peak, while both the Housing Price Index and Inflation experienced a decline.

In our view, when inflation is on the rise and Monthly Supply is low, home value tend to be high. This makes it a good time to sell residential real estate. On the other hand, when inflation is low, and Monthly Supply is high, it's a good time to consider buying residential real estate.


## Residential Real Estate Value Compared to Economic Factors



# PART 2 - Ivestment Analysis: Housing Price Index(HPI) vs S&P 500 vs The Real Estate Select Sector SPDR Fund (XLRE)

## a. Residential Real Estate Returns Compared to S&P 500 & XLRE
We started the investment analysis by importing the yfinance (Yahoo Finance), python library to pull in historical data. The yfinance tool only pulled in data back to 1985 and for that reason we narrowed our investment scope for The HPI to go back to only the start of 1985 as well. Secondly, since the HPI is a quarterly report we pulled in quarterly S&P 500 data, rather than daily or monthly records.
We then pivoted to compare The HPI to the he Real Estate Select Sector SPDR Fund (XLRE). The XLRE fund is a fund that was created towards the end 0f 2015 with their first quarterly report being 10/1/2015. This fund is a cumulation of securities of companies in the real estate industry, real estate management and development companies and REIT's. For this comparison we re-sliced the HPI data to also start with first data entry being that of 10/01/2015. Once we had our time and frequency variables in equilibrium we focused on the closing data for all three data frames then calculated and plotted the returns in 3 separate plots. The first one being quarterly returns of HPI & S&P 500 since 1985. The second plot contains quarterly returns for HPI & XLRE since 10/01/2015. The very last plot is all 3 data sets against each other, again from 10/01/2015, to keep the variables even. 

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/S&P500_and_HPI_Returns.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/XLRE_HPI_Returns.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/XLRE_HPI_SP500_Returns.png?raw=true)

## b. Sharpe Ratios and Correlation of the Rteurns between HPI, XLRE & S&P 500
After merging all 3 data sets into one single data frame we then calculated the standard deviation of all 3 assets so that we could in turn calculate and plot the Sharpe Ratios, which is a measure of risk-adjusted return on investment. For the Risk Free Rate on the standard deviation we used The 13-Week T-bill Treasury Index (^IRX). Afterwards we also plotted the correlation between the HPI, XLRE & SP 500 to analyze how each 3 move with each other. 
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Std_Dev.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Sharpe.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Inv_Corr.png?raw=true)


#### Analysis Results
* Residential Residential Real Estate is by far the most stable and consistent of the 3 asset classes, indicating less price swings and less uncertainty in the future value of your asset. 
* S&P 500 is extremely volatile when compared to The HPI and actual physical residential real estate. Even in the housing market crash of 2007 the negative returns were miniscule (about a 10% drop from 2005-2010) as compared to the S&P 500 crash from 2007-2009, resulting in a loss of value of around 20%. 
* Looking at the returns between all 3 assets, it is easy see that the XLRE very closely mirrors the S&P 500. We suspect that this is because this fund is composed of real estate securities and not of physical real estate itself. 
* Minus the real estate crash of 2007 and the mortgage crisis of 2021-2022, there is almost major price swing of Real Estate going back to 1985 and in fact usually has very small price increases/decreases per year, which on the graph looks stagnant, this is due to the fact that the price residential real estate is 1000x the price of a single share of any given stock so increase are very small in percentage terms and also the fact the real estate generally does not lose lot of value, which makes it a very logical and safe investment. 
* The HPI has a very weak, and slight negative, correlation with the XLRE. The correlation is a little stronger, though still negative with the S&P500. This means that residential real estate as very little if at all any correlation with the securities market, even real estate securities, and that prices don't always move in the right direction with the other two, because even if the stock market has a decline the residential real estate in America, generally, still holds it's value. 
* The opposite is true for the S&P and XLRE as it hold a very strong, positive correlation. Meaning prices tend to move together in the same direction, as also show on the comparative return plot of the 3 assets. 
* While all 3 asset classes have Sharpe Ratios over 1, and therefore generally acceptable, the impressive 18.807 sharpe ratio of The HPI blows the other two out of the water, making, easily, residential housing the most sound return on your investment 

## c. Using Monte Carlo Simulations and Plot Distributions on HPI, XLRE & The S&P 500.
After conducting our investment return analysis on The HPI, XLRE & S&P 500, we took it a step further and ran a Monte Carlo Analysis on the respective asset classes. To perform the analysis we used the closing dates starting from 10-01-2015 for all 3 assets and conducted 3 separate scenarios for each asset individually, using 500 simulations for each scenario. We then plotted the simulation results and the distribution probabilities. 

###### S&P 500 Scenario 
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/MC_SP500.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Dist_SP500.png?raw=true)


###### XLRE Scenario 
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/MC_XLRE.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/DIST_XLRE.png?raw=true)

###### HPI Scenario 
![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/MC_HPI.png?raw=true)

![alt text](https://github.com/devinrosen/project1_group1/blob/main/images/Dist_HPI.png?raw=true)

#### Analysis Results
* Due to the volatile nature of the securities market you can see that both the S&P 500 has the biggest variations in outcomes, with  multiple outlier scenarios over 200% returns. Although due to the nature of the stock market as well, this simulation shows that The S&P 500 offers, by far, the largest return on investment in terms of percentages. 
* The distribution plot shows that a 95%CI of returns fall within of 0-80% returns over 30 years, with the majority of the 500 simulations ran ended with 0-50% return on your investment over 30 years. 
* The XLRE Fund also has noticeable variations in outcomes due to the volatility of the securities market, even though the securities and equites all involve real estate. Although due to this asset class not being diversified. the returns are minimized with the largest outlier having a return of only 30% in 30 years, compared to the 400% of the diversified index. 
* The XLRE distribution plot agin is very left slanted, like the S&P 500, with 95%CI of the 500 simulations falling within the first quartile of 0-8% returns, the majority of which were within 0-3% returns on investment.
* The HPI simulation scenario being the most safe choice, with all 500 scenarios having at least a 5% return over 30 years. 
* The HPI scenario also seems to be the most consistent, having the least amount of outliers, with only 1 scenario that was noticeable via a line plot. 
* The distribution plot of The HPI is the standard bell-curve plot with a 95%CI falling within around 7-14.5% return of investment, the majority of which are in the middle - around 10% return. 


### Investment Conclusion
After running our investment analysis, the revelation seems to be that residential real estate is a very safe and secure investment, which some would argue is the best investment on Earth. This is a result of extremely low price swings, in either direction, leading to a slow and steady climb in prices that can lead to generating wealth for one's self. This is shown in the astonishing 18 point sharpe ration and our Monte Carlo simulation showing 0 out of the 500 simulations losing money over a 30 year horizon, as compared with the XLRE & S&P500 simulations that had multiple scenarios losing money or no making any returns over the same 30 year horizon. 

As an investor, one should absolutely include residential homes into their total investment portfolio to, not only maximize, their returns and wealth, but also help stabilize the portfolio by diversifying into residential real estate and combating the negative returns that can happen in the securities market, as shown in our investment correlation analysis.