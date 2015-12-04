def breakup(line):
    dimensions = [int(number) for number in line.split("X")]
    dimensions.sort()
    return dimensions
