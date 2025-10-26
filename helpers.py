import random
import string

class Helper:

    @staticmethod
    def generate_email():
   
        login_part = ''.join(random.choices(string.digits, k=5))
        domain = random.choice(["ya.ru", "yandex.ru", "gmail.com"])
        return f"{login_part}@{domain}"

    @staticmethod
    def generate_password(length=8):

        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))
