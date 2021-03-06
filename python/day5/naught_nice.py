def niceness(string):
    return contains_evil(string) and has_enough_vowels(string) and has_double_letter(string)


def contains_evil(string):
    evil_strings = ["ab", "cd", "pq", "xy"]
    for evil in evil_strings:
        if evil in string:
            return False
    return True

def has_enough_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for character in string:
        if character in vowels:
            vowel_count += 1

    return vowel_count >= 3

def has_double_letter(string):
    last = ""
    for character in string:
        if character == last:
            return True
        last = character

    return False

def new_niceness(string):
    return has_xYx(string) and double_pair(string)

def has_xYx(string):
    last = ""
    laster = ""
    for character in string:
        if character == laster:
            return True
        laster = last
        last = character
    return False

def double_pair(string):
    last = ""
    for index, character in enumerate(string):
        pair = last + character
        if (len(pair) == 2):
            if pair in string[index + 1:]:
                return True
        last = character

    return False
