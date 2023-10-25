def encapsulate_html(article):
    full_article = ""
    full_article += """<!doctype html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" 
    content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"> <meta 
    http-equiv="X-UA-Compatible" content="ie=edge"> <title>Document</title> </head> <body> <link rel=\"stylesheet\" 
    href=\"https://www.standaard.be/v2/article-detail/cdn/fragment-article-detail.0.0.792.ds.styles.css\">"""
    full_article += article
    full_article += """
    </body>
    </html>"""
    return full_article
