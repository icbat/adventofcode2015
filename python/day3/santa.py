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
        if character == 'v':
            y -= 1
        houses.add((x, y))
    houses_visited = len(houses)
    print ("Santa visited " + str(houses_visited) + " houses")
    print (str(houses))
    return houses_visited
