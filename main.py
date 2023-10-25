from accounts.usercreator import Creator
from webdriver.appdriver import Driver
import os
from utils.html_creator import encapsulate_html

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
full_article = encapsulate_html(article)
file.write(full_article)
file.close()
driver.close()