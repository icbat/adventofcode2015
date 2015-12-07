def niceness(string):
    return contains_evil(string) and has_enough_vowels(string)


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
