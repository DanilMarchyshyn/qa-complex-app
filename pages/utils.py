import random
import string


def random_num():
    """Generate random number"""
    return str(random.randint(111111, 999999))


def random_str(length=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def random_spc(length=5):
    """Generate random special symbols"""
    return ''.join(random.choice(string.punctuation) for _ in range(length))


class User:

    def __init__(self, username="", email="", password="", username2sym="", usernameempty="", username31sym="",
                 usernamespace="", usernamespecial=""):
        self.username = username if username else f"{random_str()}{random_num()}"
        self.username2sym = username2sym if username2sym else f"{random_str(2)}"
        self.username31sym = username31sym if username31sym else f"{random_str(31)}"
        self.usernameempty = usernameempty if usernameempty else f"{random_str(0)}"
        self.usernamespace = usernamespace if usernamespace else f"{random_str()}{random_num()}a a"
        self.usernamespecial = usernamespecial if usernamespecial else f"{random_spc()}{random_num()}"
        self.email = email if email else f"{self.username}@mail.com"
        self.password = password if password else f"{random_str(7)}{random_num()}"
