# Prosper Loan Data Findings

### by Tristen Wallace

## Dataset

There are 74,019 loan listings in the dataset with 18 variables (excluding the ID variable for identifying loan listings) for our exploration. The variables are almost split between qualitative and quantitative. Of the quantitative features, there is one date (Loan Origination), two discrete (Term, InvestmentFromFriendsCount), and the rest are continuous. Of the qualitative, 2 are ordinal (IncomeRange, CreditRating), while the remaining are nominal.

For detailed explanations of these variables, a [data feature dictionary](https://www.google.com/url?q=https://docs.google.com/spreadsheet/ccc?key%3D0AllIqIyvWZdadDd5NTlqZ1pBMHlsUjdrOTZHaVBuSlE%26usp%3Dsharing&sa=D&ust=1554486256024000) is provided.

## Summary
In the exploration, we focused on 6,123 listings between 1 July 2008 and 31 December 2009, and examined selective attributes on borrower and loans, time series events to see their effects on loan listing distributions.

In univariate exploration, we found:

- The findings revealed that the majority of loan listings were intended for debt consolidation, with most borrowers being professionals, the highest concentration of listings coming from California, and a typical income range of $25k-75k.
- `Charged Off` and `Defaulted` made up a much higer portion of loan statuses than to be expected (40.8% combined). This is worth exploring further.
- The tendency for loans to be taken out in multiples of $5k and the fact that loans of $15k and $10k are the second and thrid most frequent was fascinating.

In bivariate exploration, we found: 

- by comparing Loan Status to several different features we found that "Charged Off" and "Defaulted" loans had on average a higer debt to income ratio and Borrower APR than "Completed" or "Current" loans. 

- We discovered two interesting things about two specific Listing Catagories: "Personal" and "No Occupation"  
    - They had a higher proportion of "Charged Off" and "Defaulted" loans (more than 20% higher in most cases).
    - They accounted for 9.8% of all loans, but only existed between 2007 and 2008.

In multivariate exploration, we added new related features to our bivariate distributions in order to strengthen our findings. We found:

- Loan amount, Listing category and Time Period help to reveal the quantitative affect on listing categories during our time period of interest.
- The three features Time, Outstanding Balance and Delinquent amount produce a clear trend between amount borrowed and the concentration of delinquincies during our time period of interest.
- Adding a third feature "Occupation" to the bivariate plot of loan amount by state reveals that some occupations have more variation in loan amount than others

By conducting univariate, bivariate, and multivariate analyses, we gained insights into the characteristics of Prosper borrowers, loan listings, and time periods within the dataset. This comprehensive exploration helped us understand how these factors influenced the distribution of loans and potential for delinquency. Additionally, we observed the impact of three major historical events on Prosper loan listings during the period from March 1, 2008, to December 31, 2009.

## Key Insights for Presentation

Our presentation aims to showcase the impact of various borrower attributes, loan features, and specific time events on the distribution of Prosper loan listings. We'll begin by examining the listings from a univariate perspective, looking into the distrubtions of individual features.

Next, we'll enrich this analysis by introducing an additional attribute to these univariate distributions, observing how this changes the overall listing landscape.

Finally, our focus shifts to a more comprehensive multivariate approach. Here, we'll incorporate both Loan Amount and time series factors into our bivariate distributions, illustrating their combined effect on loan status.

## References
[A Complete Guide to Grouped Bar Charts](https://chartio.com/learn/charts/grouped-bar-chart-complete-guide/)
[Seaborn Color Palettes](https://www.practicalpythonfordatascience.com/ap_seaborn_palette)
[Horizontal boxplot with observations](https://seaborn.pydata.org/examples/horizontal_boxplot.html)