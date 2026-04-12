import time
import random
import socket
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def wait_for_selenium(host, port, timeout=60):
    start_time = time.time()
    while True:
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except (OSError, ConnectionRefusedError):
            if time.time() - start_time > timeout:
                return False
            time.sleep(2)

def run_simulation():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage") 
    try:
        driver = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            options=options
        )
        
        driver.get("http://bookstack:80/login") 
        
        time.sleep(random.randint(5, 20))
        driver.quit()
    except:
        pass

if __name__ == "__main__":
    if wait_for_selenium('selenium', 4444, timeout=90):
        time.sleep(10)
        while True:
            run_simulation()
            time.sleep(random.randint(30, 60))