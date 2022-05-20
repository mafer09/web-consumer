from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)


# def test_eight_components():
# driver = webdriver.Chrome()

driver.get("https://google.com")

print(driver.title)
driver.quit()

# driver.implicitly_wait(0.5)

# search_box = driver.find_element(by=By.NAME, value="q")
# search_button = driver.find_element(by=By.NAME, value="btnK")

# search_box.send_keys("Selenium")
# search_button.click()

# search_box = driver.find_element(by=By.NAME, value="q")
# assert search_box.get_attribute("value") == "Selenium"



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By

# service = ChromeService()
# driver = webdriver.Chrome(service=service)

# # driver = webdriver.Chrome()

# driver.get("https://www.google.com")

# driver.title

# driver.implicitly_wait(0.5)

# search_box = driver.find_element(By.NAME, "q")
# search_button = driver.find_element(By.NAME, "btnK")

# search_box.send_keys("Selenium")
# search_button.click()

# driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"

# driver.quit()