import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def simulate_user():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    try:
        base_url = "http://bookstack"
        driver.get(base_url)
        time.sleep(2)

        for _ in range(5):
            links = driver.find_elements(By.TAG_NAME, "a")
            if not links:
                break

            link = random.choice(links)
            href = link.get_attribute("href")

            if href:
                driver.get(href)
                time.sleep(random.uniform(1, 3))

        driver.get(base_url)
        time.sleep(1)

    finally:
        driver.quit()


if __name__ == "__main__":
    for _ in range(10):
        simulate_user()
        time.sleep(random.uniform(1, 4))