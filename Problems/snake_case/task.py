the_string = str(input())
word: str = ""
for char in the_string:
    if char.islower():
        word += char
    elif char.isupper():
        word += "_" + char.lower()

print(word)
