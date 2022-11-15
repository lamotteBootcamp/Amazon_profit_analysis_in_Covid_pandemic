# Project1Team6
Shared repository for Team 6


We found an article stating that Amazon profits increased 220% throughout the pandemic. We want to analyze weekly Covid cases versus Amazon stock data to see if there's a correlation between increases in cases and rises in Amazon stock. We also wanted to compare this to Walmart's stock to see if there were any variations. 

The questions we wanted answered were:
1. Did the release of the vaccine have a strong impact on the correlation on new covid cases and new covid deaths?
2. Did the stock values for Amazon fluctuate around the time of the first release of the Covid-19 vaccine?
3. Describing the effect of new covid cases and deaths on Amazon stock volume and weighted average price, which time offset(s) have the strongest correlation (r-value)?
4. How do the trends in Covid statistics and Walmart stock values compare?

------


1. Did the release of the vaccine have a strong impact on the correlation between new covid cases and new covid deaths?

We asked this question because we were interested in covid’s impact on Amazon’s stock over the course of the pandemic. This question specifically helped us get a baseline of covid data and how it changed before and after the vaccine.
To answer the question, we asked about whether covid cases and deaths were correlated, we needed to gather data about covid cases and deaths over time.

For Data Cleanup & Exploration
The data concerning Covid-19 case reporting was gathered in a CSV from the World Health Organization. The CSV contains data about new covid cases, cumulative covid cases, new covid deaths, and cumulative covid deaths over the period of 2 years for all countries that reported it. The cleanup came by removing all countries except the USA, and removing all rows that did not report new cases. New cases were only reported once a week in the US. Data was split by Date on 4/19/2021 as the established date as the wide release for the vaccine.


Data Analysis
The first steps to analyze the data was to make line plots comparing new covid cases and new covid deaths before and after the vaccine
The amount of cases skewed the y-axis so that new covid deaths was a straight line at the bottom and nothing of significance could be determined.
After the line plots, scatter plots were created to determine if there was any correlation between covid cases and deaths before and after the vaccine.

After the line plots, scatter plots were created to determine if there was any correlation between covid cases and deaths before and after the vaccine.
The r squared value was 0.62 before the vaccine and 0.26 after the wide release of the vaccine.

We were able to answer this question satisfactorily and found that there was a stronger correlation between new cases and new deaths before the vaccine was released, with an r squared value of 0.62, as opposed to 0.26 after the vaccine was widely released.

Discussion
·     After the completion of the data analysis, the results were in line with what we expected. Deaths had a higher correlation to cases before the vaccine was released. This makes sense because after the vaccine was released the death rate for covid dropped. Based on the analysis we can conclude that covid cases and deaths were more highly correlated in the US before the release of the vaccine.
Post Mortem
·     If there was more time to do research on this topic I would have compared the data to other countries aside from the US. This would help us to better determine the vaccine’s effect on the correlation between covid cases and death.

DONE
------

2. Did the stock values for Amazon fluctuate around the time of the first release of the Covid-19 vaccine?

The code for this segment can be found in the folder labelled 'James', and it is the Jupyter Source file titled 'Amazon_James'

For 2 years the coronavirus had persisted until the first vaccine was released on April 19, 2021. We wanted to see if there was a correlation between the release of the vaccine and the stock values for Amazon. 
We monitored the stock values from the beginning of 2020, until the date of the vaccine release which became our time frame for the pre-vaccine period. Then we monitored the time frame from April 19th to the end of 2021 and had that span of time as our post-vaccine period. 

For Data Cleanup & Exploration

We collected our stock data from Amazon using the website polygon.io rest API. We drew this data to encompass the span of time from January 1st, 2020 to January 1st 2022. 
The first portion of this was taking the cleaned and relabelled csv file of the Amazon stock data and we filtered this list for both the pre-vaccine and post-vaccine time frames separately, as was done previously. 
The list was split between the two sides of April 19, 2021. 
After partitioning the data by time frame, we filtered the list further to search for all Mondays through each time period. The World Health Organization updated their infection/death list for the United States weekly on Monday.


Data Analysis
We intended to graph this data correlated over time on a line graph. This graph covered the Date and Closing Stock of Amazon. 
For the pre-vaccine portion of our time frame, we see a consistent climb in Amazon’s closing stock. Their stock nearly doubles by the time of the first vaccine release. 

In the post-vaccine period, we see that their closing stock fluctuates over the period of the next 7 months before 2021’s closing. 
By the end of the year, their closing stock has remained unchanged from April’s.

Discussion
After analyzing the data, it fell in line with out original statement that their overall profits doubled over the course of the pandemic. 
If there was more time for research, we may try to find more comprehensive documentation for Amazon's stock values. When filtered it was discovered that in the list there were missing entries for certain days or weeks. This may need to be included in the margin of error with our current data reporting.

DONE

------

3. Describing the effect of new covid cases and deaths on Amazon stock volume and weighted average price, which time offset(s) have the strongest correlation (r-value)?
The coding for this segment can be found in the file marked 'Sam' and found under the Jupyter files labelled:

Over the two years of coronavirus data, Amazon stock price went up dramatially. I wanted to show a correlation between case and death reporting and Amazon stock price and trading volume. 
The theory is that stock price will go up based on increased coronavirus cases and/or deaths. 

For Data Cleanup & Exploration
For this task, there is code for seeting offsets in the number of business days. It was assumed that five days equals a work week for the Amazon data, due to Monday through Friday stock reporting. 
Similarly, 22 business days was assumed equal to a month. 1 to 3 week and 1 to 12 month date offsets were used to compare data correlation.


Data Analysis
Scatter plots were used to show correlation between new cases/stock price, new cases/stock volume, new deaths/stock price and new deaths/stock volume.
R-squared values were calculated for each date offset and the 7 month and 1 month offsets were found to have the strongest correlations.

Discussion
We showed a positive correlation between new cases and stock price at the 1 and 7 month date offsets. We showed a negative correlation between new cases and stock volume at the 1 and 7 month date offsets. 
New deaths had no significant correlation to either stock price or stock volume. This is interesting because even though death is a more significant event than confirmed case, people seem to not behave rationally in response to the news of increases in the new case count.

4. How do the trends in Covid statistics and Walmart stock values compare?

The code for this segment can be found in the folder marked 'Matusola' in the file marked walmartdata-Copy1.ipynb


For Data Cleanup & Exploration
We had to gather covid data and Walmart stock information into the same dataset. So both were merged together by date in order to get the primary data source that was used to generate the graphs. 

Data Analysis
We used a graph with two y-axis set to different ratios comparing new cases to volume weighted average price, with the date on the x-axis. We can see a correlation over time that both counts increase begin in the month of Apriil 2020. Starting in the summer of 2020 to January of 2021, there is a huge spike in new cases and volume weighted average price, showing that Walmart made their largest pandemic gains during the same time where covid made it's biggest increase in new cases. 

For the second graph, it is a ratio line graph to see the relationship between new covid deaths per day, new cases per day and Walmart's volume weighted average price. In this graph we can see a correlation between deaths and cases as we expected. This graph does not show as much correlation between covid cases and deaths with the volume weighted average price as we expected. But it is interesting to look at in adding another variable on top of new cases. 

Discussion
The first graph showed a stronger correlation than the second. New cases and volume weighted average price were strongly correlated as cases increased, Walmart's stock we up with it.


Next Steps for Further Analysis
Analyze more stock tickers, or index funds too
Data from other countries
Meta analysis of small vs. large business metrics during covid time period
    Number of businesses (total, started, closed)
    Statistics for people reported as “self-employed”
Algorithm to find highest slopes and r-squared values

Data Limitations:
Amazon stock price (NASDAQ: AMZN) doesn’t have a direct relationship with growth of the fulfillment division of the business
    AWS is a huge part of Amazon, largely affecting its stock price
    Stock Price is more a function of investor perception than actual profits/revenue
The Amazon stock price list has gaps of missing entries in occasional periods of time. This may affect representation. 
In the World Health Organization’s database, information was aggregated on a weekly basis. We could not find a database that had this information tallied daily.





Bibliography

“Amazon’s profit soars 220 percent as pandemic drives shopping online.” Karen Weise, The New York Times, https://www.nytimes.com/2021/04/29/technology/amazons-profits-triple.html. 04/29/2021

"Amazon Stock Data" Polygon.io, Polygon.io, https://polygon.io/stocks Accessed 11/2/2022

“Daily Cases and Deaths by Date Reported to WHO.” WHO Coronavirus (COVID-19) Dashboard|WHO Coronavirus(COVID-19) Dashboard With Vaccination Data, World Health Organization, https://covid19.who.int/data. Accessed 11/2/2022