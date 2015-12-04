def count_parens(text):
    openParens = [character for character in text if character == "("]
    closedParens = [character for character in text if character == ")"]
    return len(openParens) - len(closedParens)
