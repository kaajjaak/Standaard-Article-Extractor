from accounts.usercreator import Creator
from webdriver.driver import Driver
import os

driver = Driver().get_driver()
generator = Creator(driver)

email, password = generator.register()
print(email, password)
article = generator.get_article("https://www.standaard.be/cnt/dmf20231019_97764318", email, password)
print(article)
# delete file if already exists
if os.path.exists("article.html"):
    os.remove("article.html")
file = open("article.html", "w", encoding="utf-8")
file.write('<link rel="stylesheet" href="https://www.standaard.be/v2/article-detail/cdn/fragment-article-detail.0.0.792.ds.styles.css">')
file.write(article)