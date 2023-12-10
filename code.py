

from selenium import webdriver

import time
import pandas as pd




driver_path = r"C:\\Sel-chrome\\chromedriver.exe"




options = webdriver.ChromeOptions()




options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')


driver = webdriver.Chrome(driver_path, chrome_options = options)



url = "https://airtable.com/shrWxNV1xJGDRW0pj/tbl08Q4Ks1CkLBZ1D?backgroundColor=red&viewControls=on"
driver.get(url)


time.sleep(10)


lst = []
cols = ["Full name", "Job title", "Country"]

Full_name = driver.find_elements('xpath', '//*[contains(concat( " ", @class, " " ), concat( " ", "primary", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "overflow-hidden", " " ))]')
Job_title = driver.find_elements('xpath', '//*[contains(concat( " ", @class, " " ), concat( " ", "read", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "truncate", " " ))]')
Country = driver.find_elements('xpath', '//*[contains(concat( " ", @class, " " ), concat( " ", "read", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "truncate-pre", " " ))]')

for (Full_name, Job_title, Country) in (zip(Full_name, Job_title, Country)):
    lst.append((Full_name.text, Job_title.text, Country.text))

#for (Full_name, Job_title, Country) in (zip(Full_name, Job_title, Country)):
#    print(Full_name.text, Job_title.text, Country.text)
#    print("\n")

driver.quit()

df = pd.DataFrame(lst, columns= cols)

df.to_csv("Female.csv")





