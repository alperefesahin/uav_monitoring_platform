import random
import string

def generate_random_image_url():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f'http://example.com/images/{random_string}.jpg'
