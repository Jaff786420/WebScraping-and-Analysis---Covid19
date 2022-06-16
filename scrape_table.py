# Import Libraries
import pandas as pd
from selenium import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Chrome WebDriver used for the extraction of data from Chrome WebBrowser
driver = webdriver.Chrome(executable_path = 'E:\\JAFFAR\\Data Analytics Projects\\CloudyML\\WebScraping - Covid19\\chromedriver.exe')

# Link to fetch data from
driver.get('https://www.covid19india.org/')

# Timeout Series where it searches from the page 'class_name' and provides the info
timeout = 10
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "Table")))
except TimeoutException:
    driver.quit()
    
# State Wise Cases Distribution
category_element = driver.find_element(By.CLASS_NAME, "Table").text
#print(category_element)

category_list = category_element.split('\n')
#print(category_list)

# 'up arrow' symbol
up_arrow = chr(8593)
down_arrow = chr(8595)

# print(temp)
# print(up_arrow)
# print(down_arrow)

for x in category_list:
    for y in range(len(x)):
        i = x[y]
        
        if i == up_arrow:
            category_list.remove(x)
            
        if i == down_arrow:
            category_list.remove(x)

#print(category_list)
# print(len(category_list))
total_row = (len(category_list)-2)/7 # to count number of rows
#print('Total Rows: ', total_row)

# empty list for table to create a DF
data_table = []

# loop to put data into 'data_table'
i = 2
j = 9
num_row = 0
count = 9

while num_row < total_row:
    temp_list = []
    
    while i < j:
        temp_list.append(category_list[i])
        i = i + 1
        count = count + 1
    
    data_table.append(temp_list)
    j = count
    num_row = num_row + 1

#print(data_table)

column_names = data_table[0]
data_table.pop(0)

#print('New Data: \n', data_table)

# list to DF
df = pd.DataFrame(data_table, columns = column_names)
print(df)

# data to CSV
df.to_csv('covid19_data.csv')

driver.quit()