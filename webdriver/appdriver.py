from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def get_driver(self) -> webdriver:
        return self.driver

    def close_driver(self):
        self.driver.close()
