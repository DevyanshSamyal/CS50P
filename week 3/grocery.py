cart={}

while True:
    
    try:
        grocery = input().upper()
    except EOFError:
        break

    if grocery in cart:
        cart[grocery] += 1
    else:
        cart[grocery] = 1
    

for i in sorted(cart):
    print(cart[i], i)

