import wrapping_paper_dimensions

def test_breakup():
    dimensions = wrapping_paper_dimensions.breakup("2X3X4")

    assert len(dimensions) == 3
    assert dimensions[0] == 2
    assert dimensions[1] == 3
    assert dimensions[2] == 4

def test_breakup_sorts():
    dimensions = wrapping_paper_dimensions.breakup("5X4X3")

    assert len(dimensions) == 3
    assert dimensions[0] == 3
    assert dimensions[1] == 4
    assert dimensions[2] == 5
