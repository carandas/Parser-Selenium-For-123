import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import mechanize

def open():
    proxy = "72.10.160.90:11463"
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    chrome_options.add_argument(f'--proxy-server={proxy}')
    driver = uc.Chrome(
        options=chrome_options
    )
    driver.implicitly_wait(5)
    driver.get("https://www.ipqualityscore.com/login")
    time.sleep(20)
def main():
    open()


if __name__ == "__main__":
    main()