string=input("Greetings: ")

x=string.strip().lower().split()
x=x[0].removesuffix(",")

if x == "hello":
    print("$0")
elif x.startswith("h") == True :
    print("$20") 
else:
    print("$100")
