from accounts.usercreator import Creator
from webdriver.appdriver import Driver
import os
from utils.html_creator import encapsulate_html

import argparse


def main():
    parser = argparse.ArgumentParser(description="Tool to extract pay-walled articles from the standaard.be website")

    # Define the 'url' argument
    parser.add_argument("url", help="URL to be processed")

    # Define an optional argument for piping output
    parser.add_argument("--pipe", action="store_true", help="Pipe the output instead of writing to the default file")

    # Parse the arguments
    args = parser.parse_args()

    if not args.pipe:
        # Access and print the 'url' argument
        print(f"Processing URL: {args.url}")

    driver = Driver().get_driver()
    generator = Creator(driver)

    email, password = generator.register()
    article = generator.get_article(args.url, email, password)
    full_article = encapsulate_html(article)
    if args.pipe:
        print(full_article)
        return
    # delete file if already exists
    if os.path.exists("article.html"):
        os.remove("article.html")
    file = open("article.html", "w", encoding="utf-8")
    full_article = encapsulate_html(article)
    file.write(full_article)
    file.close()
    driver.close()


if __name__ == "__main__":
    main()
