alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

n = 5
codeAlphabet = alphabet

for step in range(n):
    codeAlphabet.append(codeAlphabet[0])
    codeAlphabet.pop(0)

#for letter in range(len(codeAlphabet)):
#    codeAlphabet[letter] = codeAlphabet[letter].upper()

text = "a"
codedMessage = ""

for letter in text:
    if letter == " ":
        codedMessage += " "
        continue
    posInAlphabet = alphabet.index(letter)
    codedMessage = codedMessage + codeAlphabet[posInAlphabet]
    print(codedMessage)

print(codedMessage)
