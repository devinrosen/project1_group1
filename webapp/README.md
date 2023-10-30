# Project Code Name Athena
*Goddess of reason, wisdom, and war*

The goal of the is project is to provide a set of APIs for the creation, analysis, and comparison of portfolios of assets.

## How to run the project
- `docker-compose build`
- `docker-compose up`

## Dependencies
All dependencies are included as part of the Dockerfile, docker-compose file, and requirements file.
- Dockerfile
    - [python alpine 3.9.18](https://hub.docker.com/layers/library/python/3.9.18-alpine/images/sha256-0d85a01ef353af1f5661f368cc1254d039a4c836c48a3450b36c007466e57af5)
    - [postgresql](https://postgresql.org/)
    - [bash](https://www.gnu.org/software/bash/)
- requirements.txt
    - [bokeh 3.3.0](https://bokeh.org/)
    - [cassandra-driver 3.28.0](https://github.com/datastax/python-driver)
    - [cqlsh 6.1.2](https://github.com/jeffwidman/cqlsh)
    - [Django 4.2.6](https://www.djangoproject.com/)
    - [django-cassandra-engine 1.8.0](https://github.com/r4fek/django-cassandra-engine)
    - [djangorestframework 3.14.0](https://www.django-rest-framework.org/)
    - [fredapi 0.5.1](https://github.com/mortada/fredapi)
    - [hvplot 0.9.0](https://hvplot.holoviz.org/)
    - [pandas 2.1.1](https://pandas.pydata.org/)
    - [psycopg2-binary 2.9.9](https://www.psycopg.org/)
    - [yfinance 0.2.31](https://github.com/ranaroussi/yfinance)
- docker-compose
    - [postgresql](https://postgresql.org/)
    - [cassandra](https://cassandra.apache.org/_/index.html)


## Architecture

### Data Aggregation
To expedite repeated runs of analysis, Athena can be used to aggregate data sources for assets.  Currently, the first asset class supported is stock data, via [Yahoo Finance](https://finance.yahoo.com/).  The goal is to expand the project to support more asset classes.  The storage of asset data is split into two components.
#### Series Data
Series data is saved in Cassandra with clustering by stock symbol and date.  Using Cassandra for time series data provides efficient retrieval of series data.  Cassandra partitions perform optimally when the number of elements contained is less than 100,000.  Based on this partition size and having 252 trading days in a year, a Cassandra partition would comfortably support close to 400 years of stock data per symbol.
#### Relational Data
Relational data is saved in Postgres.  Long term improvements are required for data normalization.  Currently, only a snapshot of company info is saved to Postgres.
#### Future Improvements for Data Aggregation
- Daily [cron job](https://en.wikipedia.org/wiki/Cron) to append latest entries for existing series data
- Async loading of series data when the series is not saved but part of a portfolio
- Async loading of series data that has not been added

### Portfolio
Currently portfolios generate a unique UUID when created.  They require a name, holdings data consisting of a symbol and weight, with an optional description.  Currently for portfolio analysis a plot is rendered for holding weights and a plot of cumulative daily returns of the individual stocks.
#### Future Improvements for Portfolios
- Correlation heatmap
- Beta covariance
- Sharpe ratios
- Compare portfolios to each other
- Support additional asset classes

#### General Future Improvements
- User Accounts and Auth
- Public and private portfolios
- Shareable portfolios
- Trade triggers
- Email, push, and Slack notifications
- OpenAPI Spec
