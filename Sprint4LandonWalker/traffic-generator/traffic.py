import random
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SELENIUM_URL = "http://selenium:4444/wd/hub"
BOOKSTACK_BASE_URL = "http://bookstack:80"
MATOMO_URL = "http://matomo:80"
MATOMO_SITE_ID = 1

BOOKSTACK_EMAIL = "admin@admin.com"
BOOKSTACK_PASSWORD = "password"

PAGES = [
    "/",
    "/login",
    "/books",
    "/pages"
    "/shelves"
]

def create_driver():
    print("Creating Selenium WebDriver...")
    for attempt in range(30):
        try:
            options = Options()
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Remote(
                command_executor=SELENIUM_URL,
                options=options
            )
            print("✓ WebDriver created successfully.")
            return driver
        except Exception as e:
            print(f"Attempt {attempt + 1}/30: {type(e).__name__}")
            time.sleep(2)
    raise RuntimeError("Could not create Selenium WebDriver after 30 attempts.")

def click_random_link(driver):
    try:
        links = driver.find_elements(By.TAG_NAME, "a")
        valid_links = [link for link in links if link.get_attribute("href")]
        if valid_links:
            random.choice(valid_links).click()
            time.sleep(random.uniform(2, 3))
    except Exception:
        pass

def simulate_traffic():
    print("Starting traffic simulation...")
    driver = create_driver()

    try:
        visit_count = 0
        while True:
            page = random.choice(PAGES)
            url = BOOKSTACK_BASE_URL.rstrip('/') + page
            visit_count += 1
            print(f"Visit {visit_count}: {url}")
            try:
                driver.get(url)
                time.sleep(random.uniform(2, 3))
            except Exception as e:
                print(f"  ✗ Browser error: {type(e).__name__}")
                continue

            if random.random() > 0.6:
                click_random_link(driver)
            
    except KeyboardInterrupt:
        print("\n✓ Traffic simulation stopped.")
    finally:
        driver.quit()

if __name__ == "__main__":
    try:
        simulate_traffic()
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)







