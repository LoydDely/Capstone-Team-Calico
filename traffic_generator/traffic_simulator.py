import sys
sys.stdout.reconfigure(line_buffering=True)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

def run_bookstack_traffic():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = None
    while driver is None:
        try:
            driver = webdriver.Remote(
                command_executor="http://selenium:4444",
                options=options
            )
        except WebDriverException:
            print("Waiting for Selenium...")
            time.sleep(5)


    while True:
        try:
            driver.get("http://bookstack/login")

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "email"))
            ).send_keys("admin@admin.com")

            driver.find_element(By.NAME, "password").send_keys("password")
            driver.find_element(By.NAME, "password").submit()

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "header-links"))
            )


            driver.get("http://bookstack/books")
            time.sleep(10)

            driver.execute_script("""
                _paq.push(['trackEvent','Selenium','Verification','Proxy Flow']);
            """)

            time.sleep(10)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_bookstack_traffic()