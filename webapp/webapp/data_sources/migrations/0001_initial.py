# Generated by Django 4.2.6 on 2023-10-26 00:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyOfficer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('yearBorn', models.PositiveSmallIntegerField(null=True)),
                ('fiscalYear', models.PositiveSmallIntegerField()),
                ('totalPay', models.PositiveBigIntegerField(null=True)),
                ('exercisedValue', models.PositiveBigIntegerField(null=True)),
                ('unexercisedValue', models.PositiveBigIntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Company Officer',
                'verbose_name_plural': 'Company Officers',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('address1', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('zip', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('website', models.CharField(max_length=255, null=True)),
                ('industry', models.CharField(max_length=255, null=True)),
                ('industryKey', models.CharField(max_length=255, null=True)),
                ('industryDisp', models.CharField(max_length=255, null=True)),
                ('sector', models.CharField(max_length=255, null=True)),
                ('sectorKey', models.CharField(max_length=255, null=True)),
                ('sectorDisp', models.CharField(max_length=255, null=True)),
                ('longBusinessSummary', models.TextField(null=True)),
                ('fullTimeEmployees', models.PositiveIntegerField(null=True)),
                ('auditRisk', models.PositiveSmallIntegerField(null=True)),
                ('boardRisk', models.PositiveSmallIntegerField(null=True)),
                ('compensationRisk', models.PositiveSmallIntegerField(null=True)),
                ('shareHolderRightsRisk', models.PositiveSmallIntegerField(null=True)),
                ('overallRisk', models.PositiveSmallIntegerField(null=True)),
                ('governanceEpochDate', models.PositiveIntegerField(null=True)),
                ('compensationAsOfEpochDate', models.PositiveIntegerField(null=True)),
                ('maxAge', models.PositiveIntegerField(null=True)),
                ('priceHint', models.PositiveSmallIntegerField(null=True)),
                ('previousClose', models.FloatField(null=True)),
                ('open', models.FloatField(null=True)),
                ('dayLow', models.FloatField(null=True)),
                ('dayHigh', models.FloatField(null=True)),
                ('regularMarketPreviousClose', models.FloatField(null=True)),
                ('regularMarketOpen', models.FloatField(null=True)),
                ('regularMarketDayLow', models.FloatField(null=True)),
                ('regularMarketDayHigh', models.FloatField(null=True)),
                ('dividendRate', models.FloatField(null=True)),
                ('dividendYield', models.FloatField(null=True)),
                ('exDividendDate', models.PositiveIntegerField(null=True)),
                ('payoutRatio', models.FloatField(null=True)),
                ('fiveYearAvgDividendYield', models.FloatField(null=True)),
                ('beta', models.FloatField(null=True)),
                ('trailingPE', models.FloatField(null=True)),
                ('forwardPE', models.FloatField(null=True)),
                ('volume', models.PositiveIntegerField(null=True)),
                ('regularMarketVolume', models.PositiveIntegerField(null=True)),
                ('averageVolume', models.PositiveIntegerField(null=True)),
                ('averageVolume10days', models.PositiveIntegerField(null=True)),
                ('averageDailyVolume10Day', models.PositiveIntegerField(null=True)),
                ('bid', models.FloatField(null=True)),
                ('ask', models.FloatField(null=True)),
                ('bidSize', models.PositiveIntegerField(null=True)),
                ('askSize', models.PositiveIntegerField(null=True)),
                ('marketCap', models.PositiveBigIntegerField(null=True)),
                ('fiftyTwoWeekLow', models.FloatField(null=True)),
                ('fiftyTwoWeekHigh', models.FloatField(null=True)),
                ('priceToSalesTrailing12Months', models.FloatField(null=True)),
                ('fiftyDayAverage', models.FloatField(null=True)),
                ('twoHundredDayAverage', models.FloatField(null=True)),
                ('trailingAnnualDividendRate', models.FloatField(null=True)),
                ('trailingAnnualDividendYield', models.FloatField(null=True)),
                ('currency', models.CharField(max_length=255, null=True)),
                ('enterpriseValue', models.PositiveBigIntegerField(null=True)),
                ('profitMargins', models.FloatField(null=True)),
                ('floatShares', models.PositiveBigIntegerField(null=True)),
                ('sharesOutstanding', models.PositiveBigIntegerField(null=True)),
                ('sharesShort', models.PositiveBigIntegerField(null=True)),
                ('sharesShortPriorMonth', models.PositiveBigIntegerField(null=True)),
                ('sharesShortPreviousMonthDate', models.PositiveBigIntegerField(null=True)),
                ('dateShortInterest', models.PositiveIntegerField(null=True)),
                ('sharesPercentSharesOut', models.FloatField(null=True)),
                ('heldPercentInsiders', models.FloatField(null=True)),
                ('heldPercentInstitutions', models.FloatField(null=True)),
                ('shortRatio', models.FloatField(null=True)),
                ('shortPercentOfFloat', models.FloatField(null=True)),
                ('impliedSharesOutstanding', models.PositiveBigIntegerField(null=True)),
                ('bookValue', models.FloatField(null=True)),
                ('priceToBook', models.FloatField(null=True)),
                ('lastFiscalYearEnd', models.PositiveBigIntegerField(null=True)),
                ('nextFiscalYearEnd', models.PositiveBigIntegerField(null=True)),
                ('mostRecentQuarter', models.PositiveBigIntegerField(null=True)),
                ('earningsQuarterlyGrowth', models.FloatField(null=True)),
                ('netIncomeToCommon', models.PositiveBigIntegerField(null=True)),
                ('trailingEps', models.FloatField(null=True)),
                ('forwardEps', models.FloatField(null=True)),
                ('pegRatio', models.FloatField(null=True)),
                ('lastSplitFactor', models.CharField(max_length=255, null=True)),
                ('lastSplitDate', models.PositiveIntegerField(null=True)),
                ('enterpriseToRevenue', models.FloatField(null=True)),
                ('enterpriseToEbitda', models.FloatField(null=True)),
                ('SandP52WeekChange', models.FloatField(null=True)),
                ('lastDividendValue', models.FloatField(null=True)),
                ('lastDividendDate', models.PositiveIntegerField(null=True)),
                ('exchange', models.CharField(max_length=255, null=True)),
                ('quoteType', models.CharField(max_length=255, null=True)),
                ('symbol', models.CharField(max_length=255, null=True)),
                ('underlyingSymbol', models.CharField(max_length=255, null=True)),
                ('shortName', models.CharField(max_length=255, null=True)),
                ('longName', models.CharField(max_length=255, null=True)),
                ('firstTradeDateEpochUtc', models.BigIntegerField(null=True)),
                ('timeZoneFullName', models.CharField(max_length=255, null=True)),
                ('timeZoneShortName', models.CharField(max_length=255, null=True)),
                ('messageBoardId', models.CharField(max_length=255, null=True)),
                ('gmtOffSetMilliseconds', models.BigIntegerField(null=True)),
                ('currentPrice', models.FloatField(null=True)),
                ('targetHighPrice', models.FloatField(null=True)),
                ('targetLowPrice', models.FloatField(null=True)),
                ('targetMeanPrice', models.FloatField(null=True)),
                ('targetMedianPrice', models.FloatField(null=True)),
                ('recommendationMean', models.FloatField(null=True)),
                ('recommendationKey', models.CharField(max_length=255, null=True)),
                ('numberOfAnalystOpinions', models.PositiveSmallIntegerField(null=True)),
                ('totalCash', models.PositiveBigIntegerField(null=True)),
                ('totalCashPerShare', models.FloatField(null=True)),
                ('ebitda', models.PositiveBigIntegerField(null=True)),
                ('totalDebt', models.PositiveBigIntegerField(null=True)),
                ('quickRatio', models.FloatField(null=True)),
                ('currentRatio', models.FloatField(null=True)),
                ('totalRevenue', models.PositiveBigIntegerField(null=True)),
                ('debtToEquity', models.FloatField(null=True)),
                ('revenuePerShare', models.FloatField(null=True)),
                ('returnOnAssets', models.FloatField(null=True)),
                ('returnOnEquity', models.FloatField(null=True)),
                ('grossProfits', models.PositiveBigIntegerField(null=True)),
                ('freeCashflow', models.PositiveBigIntegerField(null=True)),
                ('operatingCashflow', models.PositiveBigIntegerField(null=True)),
                ('earningsGrowth', models.FloatField(null=True)),
                ('revenueGrowth', models.FloatField(null=True)),
                ('grossMargins', models.FloatField(null=True)),
                ('ebitdaMargins', models.FloatField(null=True)),
                ('operatingMargins', models.FloatField(null=True)),
                ('financialCurrency', models.CharField(max_length=255, null=True)),
                ('trailingPegRatio', models.FloatField(null=True)),
                ('companyOfficers', models.ManyToManyField(null=True, to='data_sources.companyofficer')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
    ]