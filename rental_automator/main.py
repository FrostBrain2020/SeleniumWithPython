import Scrapper as s
from selenium import webdriver
from selenium.webdriver.common.by import By
FORM_URL = "https://forms.gle/429MCCfg67BASSEC9"

data = s.Scrapper()
driver = webdriver.Chrome()
driver.get(FORM_URL)

data_size = len(data.addresses)

for i in range(data_size):
    questions_tag = driver.find_elements(By.CSS_SELECTOR, ".Xb9hP input")
    questions_tag[0].send_keys(data.addresses[i])
    questions_tag[1].send_keys(data.price_per_month[i])
    questions_tag[2].send_keys(data.links_to_properties[i])
    send_btn_tag = driver.find_element(By.CSS_SELECTOR, ".l4V7wb span")
    send_btn_tag.click()
    if i != data_size:
        next_form_btn_tag = driver.find_element(By.CSS_SELECTOR, ".c2gzEf a")
        next_form_btn_tag.click()

driver.quit()
