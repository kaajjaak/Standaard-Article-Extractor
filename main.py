from accounts.usercreator import Creator
from webdriver.appdriver import Driver
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
file.write("""
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
""")
file.write('<link rel="stylesheet" href="https://www.standaard.be/v2/article-detail/cdn/fragment-article-detail.0.0.792.ds.styles.css">')
file.write(article)
file.write("""
</body>
</html>""")