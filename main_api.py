from fastapi import FastAPI
from accounts.usercreator import Creator
from webdriver.appdriver import Driver
from fastapi.responses import HTMLResponse
import os


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
    full_article = ""
    full_article += """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
    """
    full_article += '<link rel="stylesheet" href="https://www.standaard.be/v2/article-detail/cdn/fragment-article-detail.0.0.792.ds.styles.css">'
    full_article += article
    full_article += """
    </body>
    </html>"""
    return HTMLResponse(content=full_article, status_code=200)