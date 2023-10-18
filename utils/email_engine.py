import requests
import hashlib


# response = requests.get(url, headers=headers)
#
# print(response.json())

class Mail:
    def __init__(self):
        self.headers = {
            "X-RapidAPI-Key": "2abb15607dmsh4528ef6811f1a60p13f096jsn6883aad85d1b",
            "X-RapidAPI-Host": "privatix-temp-mail-v1.p.rapidapi.com"
        }

    def get_link_from_email(self, email):
        url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/" + self.hash_email(email) + "/"
        response = requests.get(url, headers=self.headers)
        email_text = response.json()
        if "error" in email_text:
            return "error"
        return email_text[0]["mail_text_only"].split('<a style="color: #000000; text-decoration: none;" href="')[1].split('"')[0]

    def get_domains(self):
        url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/domains/"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def hash_email(self, email):
        return hashlib.md5(email.encode()).hexdigest()

