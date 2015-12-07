def niceness(string):
    return contains_evil(string)

def contains_evil(string):
    evil_strings = ["ab", "cd", "pq", "xy"]
    for evil in evil_strings:
        if evil in string:
            return False
    return True
