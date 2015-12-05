import wrapping_paper_dimensions

def test_breakup():
    dimensions = wrapping_paper_dimensions.breakup("2x3x4")

    assert len(dimensions) == 3
    assert dimensions[0] == 2
    assert dimensions[1] == 3
    assert dimensions[2] == 4

def test_breakup_otherinput():
    dimensions = wrapping_paper_dimensions.breakup("5x4x3")

    assert len(dimensions) == 3
    assert dimensions[0] == 5
    assert dimensions[1] == 4
    assert dimensions[2] == 3

def test_calculatesides():
    actual = wrapping_paper_dimensions.calculatesides([2, 3, 4])
    print(str(actual))
    assert actual == 58

def test_calculatesides_otherinput():
    actual = wrapping_paper_dimensions.calculatesides([1, 1, 10])
    print(str(actual))
    assert actual == 43

def test_calculate_wrapping_test_data():
    assert 58 == wrapping_paper_dimensions.calculate_wrapping_paper(["2x3x4"])
    assert 43 == wrapping_paper_dimensions.calculate_wrapping_paper(["1x1x10"])

def test_wrapping_readfile():
    content = []
    with open("input.secret") as f:
        content = f.readlines()

    paper = wrapping_paper_dimensions.calculate_wrapping_paper(content)
    assert 1598415 == paper

def test_ribbon():
    assert 34 == wrapping_paper_dimensions.calculate_ribbon(["2x3x4"])
    assert 14 == wrapping_paper_dimensions.calculate_ribbon(["1x1x10"])
    assert 48 == wrapping_paper_dimensions.calculate_ribbon(["2x3x4", "1x1x10"])

def test_ribbon_to_wrap():
    assert 10 == wrapping_paper_dimensions.ribbon_to_wrap([2, 3, 4])
    assert 4 == wrapping_paper_dimensions.ribbon_to_wrap([1, 1, 10])

def test_ribbon_for_bows():
    assert 24 == wrapping_paper_dimensions.ribbon_for_bow([2, 3, 4])
    assert 10 == wrapping_paper_dimensions.ribbon_for_bow([1, 1, 10])

def test_ribbon_readfile():
    content = []
    with open("input.secret") as f:
        content = f.readlines()

    ribbon = wrapping_paper_dimensions.calculate_ribbon(content)
    print (ribbon)
    assert 3812909 == ribbon
