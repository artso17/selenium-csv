# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import re

# %%

driver = webdriver.Firefox()
driver.get('https://en.wikipedia.org/wiki/Demographics_of_Indonesia')


header = driver.find_element(By.CSS_SELECTOR,'table.wikitable:nth-child(16)')

# %%
data = header.text.split('\n')[6:]

# %%
data_trans2 = []
for d in data[:-1]:
    pattern_prov = r'^.*?(?=\d)'
    pattern_rest=r'\d.*'
    pop = re.findall(pattern_prov, d)[0].strip()
    rest = re.findall(pattern_rest,d)[0]
    rest = rest.replace(' ','_').replace(',','').split('_')
    data_trans2.append([pop]+rest)

# %%
with open('population.csv','w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['province','population_2010_cens','urban_2010_percent','tota_fertility_rate','population_2015_cens'])
    for row in data_trans2:
        csvwriter.writerow(row)

# %%
driver.quit()


