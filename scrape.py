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
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "level-vaccinated")))
except TimeoutException:
    driver.quit()
    
# Current Cases Stats, finding class 'Level' and converting it into text
current_cases_stats = driver.find_element(By.CLASS_NAME, "Level").text
#print(current_cases_stats)

cs_list = current_cases_stats.split('\n')
#print(cs_list)
print('Today Confirmed: ', cs_list[1])
print('Total Confirmed: ', cs_list[2])
print('Total Active: ', cs_list[4])
print('Today Recovered: ', cs_list[6])
print('Total Recovered: ', cs_list[7])
print('Today Deceased: ', cs_list[9])
print('Total Deceased: ', cs_list[10])

current_tested_stats = driver.find_element(By.CLASS_NAME, "VaccinationHeader").text
ct_list = current_tested_stats.split('\n')
print('Total Tested: ', ct_list[0])

# Current States Vaccination
current_states_vacc = driver.find_element(By.CLASS_NAME, "level-vaccinated")
cv = current_states_vacc.text.split('\n')[0]

vaccination_alo_prog_bar = driver.find_element(By.CLASS_NAME, "progress-bar")
vaccination_fv_prog_bar = driver.find_elements_by_class_name("label")

fvl = vaccination_fv_prog_bar[1].text
fvl = fvl.split('(')
fvl = fvl[1].split(')')

print('Total Vaccine Doses: ', cv)
print('Atleast one Dose: ', vaccination_alo_prog_bar.text)
print('Fully Vaccinated: ', fvl[0])