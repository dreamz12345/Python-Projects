from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(
    by=By.TAG_NAME, value=["title=Special:Statistics"]
).text


print(article_count)
