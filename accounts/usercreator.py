from selenium import webdriver
import requests
from utils.generator import Generator
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class Creator:
    def __init__(self, driver):
        self.driver: webdriver = driver
        self.generator: Generator = Generator()
        self.data = {
            "IsNew": True,
            "BirthDate": "12/12/1999",
            "Gender": "MALE",
            "Password": "Kaas1234",
            "IsFullUser": 0,
            "CountryCode": "BE",
            "ZipCode": "9310",
            "City": "AALST",
            "CityOfInterest": None,
            "ZipCodeOfInterest": None,
            "Street": "Achterstraat",
            "Number": "6",
            "Box": "",
            "Mobile": "",
            "Telephone": "",
            "FacebookId": None,
            "UserSubscribedNewsletters": [],
            "IsAgreedPrivacyOwn": False,
            "IsAgreedPrivacyPartner": False,
            "IsAgreedWebshop": False,
            "IsConfirmed": False,
            "CompanyFormCode": None,
            "CompanyName": None,
            "CompanyNumber": None,
            "CompanyContactPersonFirstName": None,
            "CompanyContactPersonLastName": None,
            "DoMatchOnTheFlyCall": False,
            "IsAgreedPrivacyWebshop": False
        }
        self.headers = {
            'Content-Type': 'application/json'
        }

    def register(self):
        url = "https://www.standaard.be/account/RegisterCiam"
        password = self.generator.generate_password()
        mail_address = self.generator.generate_email()
        firstname, lastname = self.generator.generate_name()

        tmp = self.data
        tmp["Email"] = mail_address
        tmp["Firstname"] = firstname
        tmp["Lastname"] = lastname
        tmp["Password"] = password

        # make post request
        response = requests.post(url, json=tmp, headers=self.headers)
        # check if "success" : True
        if response.json()["success"]:
            return mail_address, password
        else:
            return "error"

    def get_article(self, article, email, password):
        self.driver.get(article)
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
        # )
        # self.driver.find_element(By.ID, "didomi-notice-agree-button").click()
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.NAME, "emailAddress"))
        # )
        # self.driver.find_element(By.NAME, "emailAddress").send_keys(email + "\n")
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.NAME, "password"))
        # )
        # self.driver.find_element(By.NAME, "password").send_keys(password + "\n")
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Ga verder')]"))
        # )
        # self.driver.find_element(By.XPATH, "//span[contains(text(), 'Ga verder')]").click()
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Ja, akkoord')]"))
        # )
        # self.driver.find_element(By.XPATH, "//span[contains(text(), 'Ja, akkoord')]").click()


        self.wait_and_click(By.ID, "didomi-notice-agree-button")
        self.wait_and_click(By.NAME, "emailAddress")
        self.driver.find_element(By.NAME, "emailAddress").send_keys(email + "\n")
        self.wait_and_click(By.NAME, "password")
        self.driver.find_element(By.NAME, "password").send_keys(password + "\n")
        self.wait_and_click(By.XPATH, "//span[contains(text(), 'Ga verder')]")
        # self.wait_and_click(By.XPATH, "//span[contains(text(), 'Ja, akkoord')]")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//b[contains(text(), 'Dit artikel is exclusief voor abonnees, maar we bieden het je gratis aan.')]"))
        )
        return self.driver.find_element(By.XPATH, '//*[@data-fragment-name="articleDetail"]').get_attribute("outerHTML")
        # print(self.driver.page_source)
        # return self.driver.page_source

    def wait_and_click(self, by, value):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        self.driver.find_element(by, value).click()



