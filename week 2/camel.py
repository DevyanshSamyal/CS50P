name=input("camelCase: ")
string=[]

for char in name:
    if char.isupper():
        string.append("_")
    string.append(char.lower())

string = "".join(string)

print(f"snake_case: {string}")