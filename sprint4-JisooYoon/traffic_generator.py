import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# BookStack is exposed on localhost:8000 according to your compose.yaml
BOOKSTACK_URL = "http://localhost:8000"

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=chrome_options)

def visit_homepage(driver):
    driver.get(BOOKSTACK_URL)
    time.sleep(random.uniform(2, 4))

def click_internal_links(driver, max_clicks=5):
    for _ in range(max_clicks):
        links = driver.find_elements(By.TAG_NAME, "a")
        internal_links = [
            link for link in links
            if (href := link.get_attribute("href")) and href.startswith(BOOKSTACK_URL)
        ]

        if not internal_links:
            return

        link = random.choice(internal_links)
        href = link.get_attribute("href")
        driver.get(href)
        time.sleep(random.uniform(2, 4))

def simulate_user_session():
    driver = create_driver()
    try:
        visit_homepage(driver)
        click_internal_links(driver, max_clicks=6)
    finally:
        driver.quit()

if __name__ == "__main__":
    for _ in range(10):  # simulate 10 user sessions
        simulate_user_session()
        time.sleep(random.uniform(1, 3))
