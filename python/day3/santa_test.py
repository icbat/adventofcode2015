import santa

def test_santa_no_movement():
    assert 1 == santa.travel("")

def test_santa_one_move():
    assert 2 == santa.travel(">")

def test_santa_square_movement():
    assert 4 == santa.travel("^>V<")
