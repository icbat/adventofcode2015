import parens

def test_countparens_empty():
    assert 0 == parens.count_parens("")

def test_countparens_countsOpens():
    assert 1 == parens.count_parens("(")
    assert 2 == parens.count_parens("((")

def test_countparens_subtractsCloseds():
    assert -1 == parens.count_parens(")")
    assert -2 == parens.count_parens("))")
    assert -1 == parens.count_parens("())")
    assert 0 == parens.count_parens("()")

def test_findbasement_neverGotThere():
    assert -1 == parens.find_basement("")

def test_findbasement_immediately():
    assert 1 == parens.find_basement(")")

def test_findbasement_afterAWhile():
    assert 3 == parens.find_basement("())")
