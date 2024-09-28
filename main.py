import time
import csv   # Импортируем модуль сохранения csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://tomsk.hh.ru/vacancies/programmist"

driver.get(url)
time.sleep(3)

vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-card--hhzAtjuXrYFMBMspDjrF")

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, "span.vacancy-name-wrapper--tzZ1sS33pe6ELop6_Cte").text
        company = vacancy.find_element(By.CSS_SELECTOR, "span.magritte-text___tkzIl_4-3-2").text
        salary = vacancy.find_element(By.CSS_SELECTOR, "span.magritte-text_style-primary___AQ7MW_3-0-15").text
        link = vacancy.find_element(By.CSS_SELECTOR, "a.bloko-header-section-2").get_attribute("href")
    except:
        print("Mistake by parsing")
        continue
    parsed_data.append([title, company, salary, link])

driver.quit()

with open("hh.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])
    writer.writerows(parsed_data)



