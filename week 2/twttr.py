string = input("Input: ")
vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
output = []

for char in string:
    if char in vowels:
        continue
    output.append(char)

final = "".join(output)
print(f"Output: {final}")