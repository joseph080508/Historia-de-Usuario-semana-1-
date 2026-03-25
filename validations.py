def valid_text(message):
    valid = False
    while not valid:
        text = input(message)
        if text.isalpha() and text.strip():
            valid = True
        else:
            print("Invalid text, only letters allowed")
    return text

def valid_positive_float(message):
    
    valid = False
    while not valid:
        try:
            number = float(input(message))
            if number >= 0:
                valid = True
            else:
                print("Must be non-negative")
        except ValueError:
            print("Invalid number")
    return number




