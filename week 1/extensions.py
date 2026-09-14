string=input("File name: ")

x=string.strip().lower().split(".")

if x[-1] == "jpg":
    x[-1] = "jpeg"

if len(x)==1:
    print("application/octet-stream")
elif len(x)>=2:
    if x[-1] in ("png", "gif", "jpeg"):
        print("image/"+x[-1])
    elif x[-1] in ("pdf", "zip"):
        print("application/"+x[-1])
    elif x[-1] ==  "txt":
        print("text/plain")
    else:
        print("application/octet-stream")