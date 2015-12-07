import naught_nice

def test_aaa():
    assert naught_nice.niceness("aaa")

def test_ugknbfddgicrmopn():
    assert naught_nice.niceness("ugknbfddgicrmopn")

def test_lacks_contains_evil_string():
    assert False == naught_nice.niceness("haegwjzuvuyypxyu")

def test_lacks_enough_vowels():
    assert False == naught_nice.niceness("dvszwmarrgswjxmb")

def test_has_double_letters():
    assert False == naught_nice.niceness("jchzalrnumimnmhp")

def test_actual_input():
    content = []
    with open("input.secret") as f:
        content = f.readlines()

    nice_strings = 0
    for line in content:
        if naught_nice.niceness(line):
            nice_strings += 1

    print (nice_strings)
    assert 258 == nice_strings
