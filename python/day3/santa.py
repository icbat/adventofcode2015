def travel(string):
    santa = Santa()
    houses = set([santa.where_are_you()])
    for character in string:
        if character == '>':
            santa.move_right()
        if character == '<':
            santa.move_left()
        if character == '^':
            santa.move_up()
        if character == 'v':
            santa.move_down()
        houses.add(santa.where_are_you())
    houses_visited = len(houses)
    print ("Santa visited " + str(houses_visited) + " houses")
    print (str(houses))
    return houses_visited

class Santa(object):
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def where_are_you(self):
        return (self.x, self.y)
