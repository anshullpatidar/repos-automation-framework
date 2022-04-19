from selenium.webdriver.chrome.options import Options
from selenium import webdriver

class WebDriver():
    def __init__(self, page_url, headless = True):
        options = Options()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--start-maximized")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('window-size=1200,1100')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get(page_url)
        self.timeout = 90
        self.base_url = page_url