string=input("Expression: ")

x,y,z = string.split()

x,z=float(x),float(z)

if y =="+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x*z)
else:
    print(x/z)


