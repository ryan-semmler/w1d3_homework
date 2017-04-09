def clean_string(thing):
    thing = thing.lower()
    new_thing = ''
    for char in thing:
        if char.isalpha():
            new_thing += char
    return new_thing


def is_palindrome(thing):
    thing = clean_string(thing)
    if len(thing) > 2:
        if thing[0] == thing[-1]:
            if is_palindrome(thing[1: -1]):
                return True
            else:
                return False
        else:
            return False
    elif len(thing) == 2:
        return thing[0] == thing[1]
    else:
        return True


while True:
    print(is_palindrome(input()))
