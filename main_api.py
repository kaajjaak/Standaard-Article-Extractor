from fastapi import FastAPI
from accounts.usercreator import Creator
from webdriver.appdriver import Driver
from fastapi.responses import HTMLResponse
import os
from utils.html_creator import encapsulate_html


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/cnt/{article_id}")
def read_item(article_id: str):
    driver = Driver().get_driver()
    generator = Creator(driver)
    email, password = generator.register()
    article = generator.get_article(f"https://www.standaard.be/cnt/{article_id}", email, password)
    driver.close()
    full_article = encapsulate_html(article)
    return HTMLResponse(content=full_article, status_code=200)