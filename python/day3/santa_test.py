import santa

def test_santa_no_movement():
    assert 1 == santa.travel("")

def test_santa_one_move():
    assert 2 == santa.travel(">")

def test_santa_square_movement():
    assert 3 == santa.travel("^>v<")

def test_santa_back_and_forth():
    assert 3 == santa.travel("^v")
    assert 11 == santa.travel("^v^v^v^v^v")

def test_actual_from_file():
    content = []
    with open("input.secret") as f:
        content = f.readlines()

    assert 2341 == santa.travel(content[0])
