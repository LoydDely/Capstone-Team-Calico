import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpecCond
from selenium.webdriver.chrome.options import Options
import random

BOOKSTACK_URL = "http://bookstack:80"
WAIT = 10
DELAY = 5
MIN_STAY = 2
MAX_STAY = 8

def createDriver():
    chrome = Options()
    chrome.add_argument('--headless')
    chrome.add_argument('--no-sandbox')
    chrome.add_argument('--disable-dev-shm-usage')
    chrome.add_argument('--disable-gpu')
    chrome.add_argument('--window-size=1920,1080')
    chrome.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome)
    return driver

def bookstackVisit(driver):
    try:
        driver.get(BOOKSTACK_URL)
        WebDriverWait(driver, WAIT).until(
            ExpecCond.presence_of_all_elements_located((By.TAG_NAME, "body"))
        )
        stayTime = random.randint(MIN_STAY, MAX_STAY)
        time.sleep(stayTime)
        try:
            links = driver.find_elements(By.TAG_NAME, "a")
            cLinks = [link for link in links if link.get_attribute("href") and 
                             (link.get_attribute("href").startswith("http://bookstack") or 
                              link.get_attribute("href").startswith("/"))]
            if cLinks:
                for _ in range(random.randint(2, 5)):
                    try:
                        rLink = random.choice(cLinks)
                        href = rLink.get_attribute("href")
                        driver.execute_script("arguments[0].scrollIntoView();", rLink)
                        time.sleep(1)
                        driver.execute_script("arguments[0].click();", rLink)
                        WebDriverWait(driver, WAIT).until(
                            ExpecCond.presence_of_all_elements_located((By.TAG_NAME, "body"))
                        )
                        stayTime = random.randint(MIN_STAY, MAX_STAY)
                        time.sleep(stayTime)
                    except Exception as e:
                        break
        except Exception as e:
            print(f"Error during link navigation: {e}")
        return True
    except Exception as e:
        print(f"Error visiting BookStack: {e}")
        return False


def traffic():
    driver = None
    try:
        driver = createDriver()
        driver.set_page_load_timeout(WAIT)
        time.sleep(15)
        while True:
            try:
                bookstackVisit(driver)
                time.sleep(DELAY) 
            except Exception as e:
                time.sleep(DELAY)
    except Exception as e:
        print(f"Fatal error in traffic generation: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":    
    try:
        traffic()
    except KeyboardInterrupt:
        print("Traffic generator stopped by user")
    except Exception as e:
        print(f"Unhandled exception: {e}")
