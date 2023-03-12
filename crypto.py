from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options=Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.get('https://www.courscrypto.com/')

time.sleep(10)

# We retrieve the full table
table = driver.find_element(By.ID, 'cmc_coinslist')
# We retrieve the data
table_body = table.find_element(By.XPATH, './tbody')
# We retrieve the list of lines
rows = table_body.find_elements(By.XPATH, './/*')

i = 1
# For each line we retrieve the name, price and variation
for row in rows:
    # The [] allow to select the nth child of the component
    crypto_name = row.find_element(By.XPATH, '//tr[{}]/td[2]'.format(i)).get_attribute('data-sort')
    price = row.find_element(By.XPATH, '//tr[{}]/td[3]'.format(i)).get_attribute('data-sort')
    variation = row.find_element(By.XPATH, '//tr[{}]/td[4]'.format(i)).get_attribute('data-sort')
    print(crypto_name)
    print(price)
    print(variation)
    # The i allows to increment the lines to retrieve the following values
    i = i + 1
    if i == 10:
        break

driver.quit()