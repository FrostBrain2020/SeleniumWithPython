from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(chrome_options)
driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}
for n in range(len(dates)):
    events[n] = {
        "time": dates[n].text,
        "name": names[n].text,
    }

print(events)

# driver.close()  # close active tab in browser
driver.quit()  # quit entire program

# Methods after selected element
# .text
# .send_keys("input_text")
# .click()
# from selenium.webdriver.common.keys import Keys
# .send_keys(Keys.ENTER)
# .send_keys("input_text", Keys.ENTER)