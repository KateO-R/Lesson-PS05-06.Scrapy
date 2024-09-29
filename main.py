import time
import csv   # Импортируем модуль сохранения csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/ekaterinburg/category/svet"

driver.get(url)
time.sleep(7)

lights = driver.find_elements(By.CLASS_NAME, "div.WdR1o")

parsed_data = []

for light in lights:
    try:
        name = light.find_element(By.CSS_SELECTOR, "span.div.lsooF").text
        price = light.find_element(By.CSS_SELECTOR, "span.div.q5Uds").text
        link = light.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
    except Exception as e:
        print(f"Mistake by parsing: {e}")
        continue
    parsed_data.append([name, price, link])

driver.quit()

with open("lights.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'цена', 'ссылка на товар'])
    writer.writerows(parsed_data)




