def input_text(message):
    valid = False
    while not valid:
        text = input(message)
        if text.isalpha() and text.strip():
            valid = True
        else:
            print("Invalid text, only letters allowed")
    return text
    