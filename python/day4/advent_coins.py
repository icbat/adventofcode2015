import hashlib

def mine(secret_key, zeroes):

    for potential_coin in range(1500000):
        result = hash(secret_key, potential_coin)

        if starts_with_zeroes(result, zeroes):
            print("Found coin! " + str(potential_coin) + " resulted in " + result)
            return potential_coin

def starts_with_zeroes(string, zeroes):
    if len(string) < zeroes:
        return False
    for character in string[:zeroes]:
        if character != "0":
            return False
    return True

def hash(key, value):
    hasher = hashlib.md5()

    hasher.update((str(key) + str(value)).encode())
    return hasher.hexdigest()
