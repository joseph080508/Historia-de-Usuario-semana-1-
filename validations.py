def valid_text(message):
    #Valid the text
    valid = False
    while not valid:
        text = input(message)
        if text.isalpha() and text.strip():
            valid = True
        else:
            print("Invalid text, only letters allowed")
    return text

def valid_positive_float(message):
    #Valid the number is float and positive
    
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



def valid_positive_int(message):
    #Valid the number is int and positive
    valid = False
    while not valid:
        try:
            number = int(input(message))
            if number >= 0:
                valid = True
            else:
                print("Must be non-negative")
        except ValueError:
            print("Invalid number")
    return number


def valid_optional_float(message):
    #allow -1 or positive float
    valid = False
    while not valid:
        try:
            number = float(input(message))
            if number >= -1:
                valid = True
            else:
                print("Invalid value")
        except ValueError:
            print("Invalid number")
    return number

def valid_optional_int(message):
    #allow -1 or positive int
    valid = False
    while not valid:
        try:
            number = int(input(message))
            if number >= -1:
                valid = True
            else:
                print("Invalid value")
        except ValueError:
            print("Invalid number")
    return number


