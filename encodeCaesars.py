from typing import List
import sys


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# n = 5
# codeAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
#                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# text = "hallo mein name ist julius"


def shiftAlphabet(alphabet: List[str], shift: int):
    codeAlphabet = alphabet.copy()

    for step in range(shift):
        codeAlphabet.append(codeAlphabet[0])
        codeAlphabet.pop(0)

    return codeAlphabet


def encode(message, alphabet, codeAlphabet):
    codedMessage = ""

    for letter in message:
        if letter == " ":
            codedMessage += " "
            continue

        try:
            posInAlphabet = alphabet.index(letter)
            codedMessage += codeAlphabet[posInAlphabet]
        except ValueError:
            codedMessage += "%"

    return codedMessage.upper()


def handleFileInput(argv):
    try:
        path = argv[0]
        shift = argv[1]
    except IndexError:
        print("usage: encodeCaesars <file.txt> <alphabet offset>")
        sys.exit(2)

    try:
        path = str(path)
        shift = int(shift)
    except ValueError:
        sys.exit(2)

    with open(path, "r") as inputFile:
        codeAlphabet = shiftAlphabet(alphabet, shift)
        with open("results.txt", "w") as outputFile:
            outputFile.write(encode(inputFile.read(), alphabet, codeAlphabet))

    print("--- Your results are in the results.txt file ---")


def handleUserInput():
    text = input("What would you like to encode?\n")

    shift = "a"
    while type(shift) != int:
        try:
            shift = int(input("What shift value should be used?\n"))
        except ValueError:
            print("You didn't input a valid value (int)")

    codeAlphabet = shiftAlphabet(alphabet, 5)

    print(f"Encoded result:\n{encode(text, alphabet, codeAlphabet)}\n")

# codeAlphabet = shiftAlphabet(alphabet, 5)
# print(encode(text, alphabet, codeAlphabet))


def main(argv):
    if not argv:
        handleUserInput()
    else:
        handleFileInput(argv)


if __name__ == "__main__":
    main(sys.argv[1:])
