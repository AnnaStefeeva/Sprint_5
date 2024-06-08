import random
import string
from data import EMAIL_TEMPLATE


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_email():
    random_number = random.randint(100, 999)
    return EMAIL_TEMPLATE.format(random_number)
