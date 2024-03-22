Scenario: Marketing Performance Dashboard Update
A marketing team at a large company runs campaigns across multiple channels: social media, email, paid search, and their website. Each channel provides data in different formats and through different APIs. The goal is to create a unified view of the marketing performance in Datorama by pulling data from these channels, cleaning and transforming it, and then updating the dashboard to reflect the latest metrics.

Steps:
Making HTTP Requests & Working with APIs:

The first step is to collect data from various marketing channels. For example, use the Facebook Graph API to get social media engagement data, Google Analytics API for website traffic, Mailchimp API for email campaign performance, and Google Ads API for paid search metrics.
Write Python scripts using requests or httpx to make GET requests to these APIs and fetch the data.
Working with Numpy, Pandas:

Once the data is collected, use Pandas for data manipulation and Numpy for numerical operations. For instance, loading the JSON or CSV data into Pandas DataFrames for easy manipulation.
Use Pandas to merge/join data from different sources on a common key, such as campaign ID or date, to create a unified dataset.
Data Transformation and Cleaning:

Perform data cleaning operations like handling missing values, removing duplicates, and converting data types.
Transform the data into a format suitable for analysis and visualization in Datorama. This might include aggregating metrics at a daily or weekly level, calculating new metrics such as click-through rates, or normalizing data for comparison.
Bulk Mapping Update with Python:

Once the dataset is ready, the final step is to update the Datorama dashboard. This could involve using Datorama's API to bulk upload the transformed data.
Write a script to map the cleaned and transformed data to the corresponding fields in Datorama and send the data in bulk. This script would make POST requests to Datorama's API, updating the dashboard to reflect the latest marketing performance metrics.
