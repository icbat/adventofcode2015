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

def test_actual_part1():
    content = []
    with open("input.secret") as f:
        content = f.readlines()

    nice_strings = 0
    for line in content:
        if naught_nice.niceness(line):
            nice_strings += 1

    print (nice_strings)
    assert 258 == nice_strings

def test_qjhvhtzxzqqjkmpb():
    assert naught_nice.new_niceness("qjhvhtzxzqqjkmpb")

def test_xxyxx():
    assert naught_nice.new_niceness("xxyxx")

def test_repeating_with_one_between():
    assert False == naught_nice.new_niceness("uurcxstgmygtbstg")

def test_pair_appears_twice():
    assert False == naught_nice.new_niceness("ieodomkazucvgmuy")

def test_pair_appears_twice_but_not_overlapping():
    assert False == naught_nice.double_pair("aaa")

def test_actual_part2():
    content = []
    with open("input.secret") as f:
        content = f.readlines()

    nice_strings = 0
    for line in content:
        if naught_nice.new_niceness(line):
            nice_strings += 1

    print (nice_strings)
    assert 53 == nice_strings
