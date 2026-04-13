import time
import random
import requests
import hashlib
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BOOKSTACK_HOST = "bookstack"
BOOKSTACK_PORT = 80
MATOMO_HOST = "matomo"
MATOMO_PORT = 80
MATOMO_SITE_ID = "1"
SELENIUM_HOST = "selenium"
SELENIUM_PORT = 4444

def waitMatomo(host=MATOMO_HOST, port=MATOMO_PORT, timeout=90):
    url = f"http://{host}:{port}"
    start = time.time()
    while True:
        try:
            requests.get(url, timeout=5)
            return True
        except Exception:
            pass
        if time.time() - start > timeout:
            return False
        time.sleep(2)

def track(path, title, referer="", id="", time=None):
    if not id:
        id = hashlib.md5(f"visitor-{time.time()}".encode()).hexdigest()[:16]
    if time is None:
        time = datetime.utcnow()
    params = {
        'site': MATOMO_SITE_ID,
        'rec': '1',
        'url': f"http://{BOOKSTACK_HOST}:{BOOKSTACK_PORT}{path}",
        'name': title,
        '_id': id,
        'rand': str(random.randint(100000, 999999)),
        'apiv': '1',
        'image': '0',
        'cid': id,
    }
    timestamp = int(time.timestamp())
    params['cdt'] = datetime.utcfromtimestamp(timestamp).isoformat()
    if referer:
        params['urlref'] = referer
    try:
        req = requests.get(f"http://{MATOMO_HOST}:{MATOMO_PORT}/matomo.php", params=params, timeout=5)
        if req.status_code in [200, 204]:
            return True, id
    except Exception:
        pass
    return False, id

def traffic():
    pages = [
        ('/', 'Home'),
        ('/login', 'Login'),
        ('/books', 'Books'),
        ('/pages', 'Pages'),
        ('/search', 'Search'),
    ]
    stamp = random.randint(-99999, 0)
    sTime = datetime.utcnow() + timedelta(seconds=stamp)
    vID = hashlib.md5(f"visitor-{sTime.timestamp()}".encode()).hexdigest()[:16]
    nPages = random.randint(3, 7)
    referer = ""
    for i in range(nPages):
        page, title = random.choice(pages)
        sTime += timedelta(seconds=random.randint(5, 30))
        check, vID = track(page, title, referer, vID, sTime)
        if check:
            referer = f"http://{BOOKSTACK_HOST}:{BOOKSTACK_PORT}{page}"
        time.sleep(random.uniform(0.5, 2))

def SelSession():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    try:
        driver = webdriver.Remote(
            command_executor=f'http://{SELENIUM_HOST}:{SELENIUM_PORT}/wd/hub',
            options=options
        )
        print(f"  → Loading http://{BOOKSTACK_HOST}:{BOOKSTACK_PORT}/login")
        driver.get(f"http://{BOOKSTACK_HOST}:{BOOKSTACK_PORT}/login")
        wTime = random.randint(5, 20)
        time.sleep(wTime)
        driver.quit()
    except Exception as e:
        print(f"Error: {e}")

def main():
    waitMatomo(timeout=90)
    time.sleep(10)
    while True:
        try:
            SelSession()
            try:
                traffic()
            except Exception as e:
                print(f"Error: {e}")
            time.sleep(random.randint(5, 7))
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
