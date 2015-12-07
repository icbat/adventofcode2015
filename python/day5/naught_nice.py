def niceness(string):
    evil_strings = ["ab", "cd", "pq", "xy"]
    for evil in evil_strings:
        if evil in string:
            return False
    return True
