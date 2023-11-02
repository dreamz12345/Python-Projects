from selenium import webdriver
from selenium.webdriver.common.by import By
import re

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
shrubbery_elements = driver.find_elements(by=By.CLASS_NAME, value="shrubbery")
list_of_rows = shrubbery_elements[1].find_elements(by=By.TAG_NAME, value="li")
python_events = []

for row in list_of_rows:
    event = {}
    time_ = row.find_element(by=By.TAG_NAME, value="time").get_attribute("datetime")
    time_: re.Match = re.match("[0-9]+-[0-9]+-[0-9]+", time_)
    event["time"] = time_.group(0)
    event["name"] = row.find_element(by=By.TAG_NAME, value="a").text
    python_events.append(event)

for event in python_events:
    print(f"{event['time']} : {event['name']}")

driver.quit()
