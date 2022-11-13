import string
import random

available_symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits

def get_random_password(n=None) -> str:
    if n is not None:
        random_symbols_list = random.sample(available_symbols, n)
        random_password = ''.join(str(symbol) for symbol in random_symbols_list)
    else:
        random_symbols_list = random.sample(available_symbols, 8)
        random_password = ''.join(str(symbol) for symbol in random_symbols_list)
    return random_password

print(get_random_password())
