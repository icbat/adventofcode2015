def count_parens(text):
    openParens = [character for character in text if character == "("]
    closedParens = [character for character in text if character == ")"]
    return len(openParens) - len(closedParens)

def find_basement(text):
    current_floor = 0
    for instruction_number, character in enumerate(text):
        if character == "(":
            current_floor += 1
        if character == ")":
            current_floor -= 1

        if current_floor == -1:
            return instruction_number + 1

    return -1
