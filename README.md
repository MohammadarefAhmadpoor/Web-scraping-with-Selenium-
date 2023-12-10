# Selenium Web Scraping

This code is a Python script that utilizes the Selenium library to perform web scraping. The script automates the process of extracting data from a specific webpage and saves the data to a CSV file.

## Requirements

- Python
- Selenium library
- Chrome web browser
- ChromeDriver executable file (chromedriver.exe)

## Installation

1. Install Python from the official website: https://www.python.org/downloads/
2. Install Selenium library by running the following command in your terminal or command prompt:
   ````
   pip install selenium
   ```
3. Download the ChromeDriver executable file compatible with your Chrome web browser version. You can download it from the official website: https://sites.google.com/a/chromium.org/chromedriver/downloads
4. Update the `driver_path` variable in the code with the path to the downloaded ChromeDriver executable file.

## Usage

1. Import the necessary libraries:
   ````python
   from selenium import webdriver
   import time
   import pandas as pd
   ```

2. Set the path to the ChromeDriver executable:
   ````python
   driver_path = r"C:\\Sel-chrome\\chromedriver.exe"
   ```

3. Configure Chrome options:
   ````python
   options = webdriver.ChromeOptions()
   options.add_argument('--ignore-certificate-errors')
   options.add_argument('--ignore-ssl-errors')
   ```

4. Initialize the Chrome driver:
   ````python
   driver = webdriver.Chrome(driver_path, chrome_options=options)
   ```

5. Specify the URL of the webpage to scrape:
   ````python
   url = "https://airtable.com/shrWxNV1xJGDRW0pj/tbl08Q4Ks1CkLBZ1D?backgroundColor=red&viewControls=on"
   ```

6. Open the webpage using the Chrome driver:
   ````python
   driver.get(url)
   ```

7. Wait for the webpage to load:
   ````python
   time.sleep(10)
   ```

8. Extract the desired data from the webpage:
   ````python
   lst = []
   cols = ["Full name", "Job title", "Country"]

   Full_name = driver.find_elements('xpath', '//*[contains(concat( " ", @class, " " ), concat( " ", "primary", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "overflow-hidden", " " ))]')
   Job_title = driver.find_elements('xpath', '//*[contains(concat( " ", @class, " " ), concat( " ", "read", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "truncate", " " ))]')
   Country = driver.find_elements('xpath', '//*[contains(concat( " ", @class, " " ), concat( " ", "read", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "truncate-pre", " " ))]')

   for (Full_name, Job_title, Country) in (zip(Full_name, Job_title, Country)):
       lst.append((Full_name.text, Job_title.text, Country.text))
   ```

9. Close the Chrome driver:
   ````python
   driver.quit()
   ```

10. Create a DataFrame from the extracted data:
    ```python
    df = pd.DataFrame(lst, columns=cols)
    ```

11. Save the DataFrame to a CSV file:
    ```python
    df.to_csv("Female.csv")
    ```

Make sure to customize the code according to your specific requirements and adjust the XPath expressions to match the structure of the webpage you intend to scrape.

Note: Remember to handle any potential exceptions and errors that may occur during the web scraping process.