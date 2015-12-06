def travel(string):
    x = 0
    y = 0
    houses = set([(x, y)])
    for character in string:
        if character == '>':
            x += 1
        if character == '<':
            x -= 1
        if character == '^':
            y += 1
        if character == 'V':
            y -= 1
        houses.add((x, y))
    return len(houses)
