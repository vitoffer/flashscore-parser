from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import os
import time


def get_comments_with_retry(given_driver, delay=0.1):
    while True:
        try:
            return [elem.text for elem in given_driver.find_elements(By.CSS_SELECTOR, '[data-testid="wcl-commentary"]')]
        except StaleElementReferenceException:
            time.sleep(delay)


# example_link = "https://www.flashscorekz.com/match/bcDpMvcR/#/match-summary/live-commentary/0"

with open('input.txt', 'r', encoding='utf-8') as f:
    input_links = list(map(lambda x: x.strip(), f.readlines()))

firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--disable-gpu")
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Firefox(options=firefox_options)
driver.set_page_load_timeout(120)

pattern = re.compile(r"https://www\.flashscorekz\.com/match/[^/#?]+(?:/[^\s]*)?")

try:
    for input_link in input_links:
        if not pattern.match(input_link):
            print(f"Ссылка {input_link} не обработана (неверный формат)")
            continue

        driver.get(input_link)
        time.sleep(0.3)

        title_splitted = list(map(lambda x: re.sub(r'[\\/:*?"<>|]', '_', x), driver.title.strip().split(' | ')))
        short_title = title_splitted[0]
        detailed_title = title_splitted[1]

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'liveCommentary'))
            )
        except TimeoutException:
            print(f"Не удалось прочитать текстовую трансляцию матча {detailed_title} (возможно, матч еще не состоялся)")
            continue

        comments = get_comments_with_retry(driver)

        if not os.path.exists('results'):
            os.makedirs('results')

        with open(fr'results/{short_title}.txt', 'w+', encoding='utf-8') as f:
            f.write('\n\n'.join(comments))

finally:
    driver.quit()