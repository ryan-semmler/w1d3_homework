import re


def is_palindrome(sentence):
    sentence = re.sub(r'[^A-Za-z]', "", sentence)
    if sentence[0].lower() != sentence[-1].lower():
        return False
    elif len(sentence) <= 2:
        return True
    elif len(sentence) > 2:
        is_palindrome(sentence[1:-1])
    return True


def main():
    while True:
        sentence = input("Enter some text: ")
        if sentence.lower() == "quit":
            break
        if is_palindrome(sentence):
            print(sentence, "is a palindrome.")
        else:
            print(sentence, "is not a palindrome.")


if __name__ == '__main__':
    main()
