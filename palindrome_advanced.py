import re


def is_palindrome(sentence):
    sentence = re.sub(r'[^A-Za-z]', "", sentence)
    for i in range(int(len(sentence) / 2)):
        if sentence[i].lower() != sentence[-(i + 1)].lower():
            return False
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
