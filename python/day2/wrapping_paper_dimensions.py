from functools import reduce

def breakup(line):
    dimensions = [int(number) for number in line.split("x")]
    print (line + " broke in to " + str(dimensions))
    return dimensions

def double(x):
    return 2*x

def calculatesides(dimensions):
    print ("Given dimensions " + str(dimensions))
    areas = buildSortedAreas(dimensions)
    smallest_side = areas[0]

    cubic_area = sum(map(double, areas))
    return cubic_area + smallest_side

def buildSortedAreas(dimensions):
    print ("Building Areas from " + str(dimensions))
    length = dimensions[0]
    width = dimensions[1]
    height = dimensions[2]
    areas = [length * width, length * height, width * height]
    return sort(areas)

def calculate_wrapping_paper(content):
    content = cleanup(content)
    dimensions = map(breakup, content)
    paper_per_present = map(calculatesides, dimensions)
    return sum(paper_per_present)

def cleanup(content):
    def trim(string):
        return string.strip()
    return map(trim, content)

def sort(list):
    list.sort()
    return list

def calculate_ribbon(content):
    content = cleanup(content)
    dimensions = map(breakup, content)
    dimensions = list(map(sort, dimensions))
    
    all_around_presents = sum(list(map(ribbon_to_wrap, dimensions)))
    print ("all_around_presents")
    print (all_around_presents)
    all_bows = sum( map(ribbon_for_bow, dimensions))

    print (all_bows)
    return all_around_presents + all_bows

def ribbon_to_wrap(dimensions):
    smallest_sides_dimensions = dimensions[:2]
    print ("Found smallest side of " + str(smallest_sides_dimensions))
    to_wrap = reduce ((lambda x, y: x+y), map( (lambda x: x+x) , smallest_sides_dimensions))
    print ("ribbon to go around the sides: " + str(to_wrap))
    return to_wrap

def ribbon_for_bow(dimensions):
    return reduce( (lambda x, y: x * y), dimensions )
