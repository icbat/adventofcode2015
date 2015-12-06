def travel(string):
    santa = Santa()
    robo_santa = Santa()
    houses = set([santa.where_are_you()])
    for index, character in enumerate(string):
        if (index % 2 == 0):
            active_santa = santa
        else:
            active_santa = robo_santa
        if character == '>':
            active_santa.move_right()
        if character == '<':
            active_santa.move_left()
        if character == '^':
            active_santa.move_up()
        if character == 'v':
            active_santa.move_down()
        houses.add(active_santa.where_are_you())
    houses_visited = len(houses)
    print ("Santa visited " + str(houses_visited) + " houses")
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
