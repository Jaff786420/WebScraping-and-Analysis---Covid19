# WebScraping-and-Analysis---Covid19

Simple Analysis performed on Covid19 data exracted from website "https://covid19india.org/".

Python language was used to Scrape data from the website and converted that into CSV file and analysis was performed in Tableau Public.

## 1. Web Scarping using Python

Python script is written where we extract the data/table from the website.

As i have used 'Chrome' browser, i will be using Chrome WebDriver (chromedriver.exe) which is used in the script so that the script understands from which website it needs to fetch the details.

I have used 'Selenium' library to extract details as the Covid19 website is a Dynamic Website and Selenium is the best library to fetch Dynamic data.

After the data is fetched from the website, which will be in the List format, we will be converting it into DataFrame using Pandas and download the same into CSV file (covid19_data.csv).