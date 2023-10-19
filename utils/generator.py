from faker import Faker
from password_generator import PasswordGenerator


class Generator:
    def __init__(self):
        self.faker = Faker()
        self.pwg = PasswordGenerator()

    def generate_name(self):
        return self.faker.name().split(' ')

    def generate_password(self):
        return self.pwg.generate()

    def generate_username(self):
        return self.faker.user_name()

    def generate_email(self):
        return self.faker.email()


generator = Generator()

print(generator.generate_username())
