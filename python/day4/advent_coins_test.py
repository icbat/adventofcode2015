import advent_coins

def test_mine_abcdef():
    assert 609043 == advent_coins.mine("abcdef", 5)

def test_mine_pqrstuv():
    assert 1048970 == advent_coins.mine("pqrstuv", 5)

def test_starts_with_five_zeroes():
    assert True == advent_coins.starts_with_zeroes("00000", 5)
    assert True == advent_coins.starts_with_zeroes("00000b", 5)
    assert False == advent_coins.starts_with_zeroes("100000b", 5)
    assert True == advent_coins.starts_with_zeroes("000001", 5)
    assert False == advent_coins.starts_with_zeroes("0000", 5)

def test_hash_matches_assumption():
    hashed = advent_coins.hash("abcdef", "609043")
    assert advent_coins.starts_with_zeroes(hashed, 5)

    hashed = advent_coins.hash("pqrstuv", "1048970")
    assert advent_coins.starts_with_zeroes(hashed, 5)

def test_mine_for_real():
    assert 254575 == advent_coins.mine("bgvyzdsv", 5)
    assert 1038736 == advent_coins.mine("bgvyzdsv", 6)
