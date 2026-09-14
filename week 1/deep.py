string=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if string.strip() == "42":
    print("Yes")
elif string.lower().strip() == "forty-two":
    print("Yes")
elif string.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")    
