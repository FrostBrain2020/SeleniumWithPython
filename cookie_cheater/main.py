from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
MINUTES = 5
URL = "https://orteil.dashnet.org/experiments/cookie/"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")
cookie_per_second = driver.find_element(By.ID, "cps")

end_time = datetime.datetime.now() + datetime.timedelta(seconds=60 * MINUTES)
per_second = 0
while datetime.datetime.now() < end_time:
    cookie.click()
    per_second = cookie_per_second.text
    if datetime.datetime.now().second % 5 == 0:
        products = driver.find_elements(By.CSS_SELECTOR, "#store div")
        for product in products[::-1]:
            if product.get_attribute("class") == "":
                print(product.tag_name)
                print(f"buy: {product.text.strip()}")
                product.click()
        products.clear()

print(f"Final Score per second: {per_second}")

