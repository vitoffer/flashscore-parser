from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

example_link = "https://www.flashscorekz.com/match/bcDpMvcR/#/match-summary/live-commentary/0"

# print("Введите ссылку:")
# input_link = input()

input_link = example_link

pattern = re.compile(r"https://www\.flashscorekz\.com/match/bcDpMvcR/?(#.*)?")

while not pattern.match(input_link):
    print("Неверный формат ссылки, попробуйте еще раз:")
    input_link = input()

firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--disable-gpu")
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Firefox(options=firefox_options)

driver.get(input_link)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'liveCommentary'))
    )
    res = '\n\n'.join(list(map(lambda elem: elem.text, element.find_elements(By.CSS_SELECTOR, '[data-testid="wcl-commentary"]'))))
finally:
    driver.quit()

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(res)