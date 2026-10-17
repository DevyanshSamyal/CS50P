def main():

    percentage=convert_fraction()
    print(fuel_meter(percentage))

def convert_fraction():
    while True:
        fraction = input("Fraction: ")

        try:
            x,y = fraction.split("/")
            x,y = int(x), int(y)
        except ValueError:
            continue

        if x>y or x<0:
            continue

        try:
            return x/y * 100
        except ZeroDivisionError:
            continue

def fuel_meter(s):
    if s <=1:
        return "E"
    if s <99:
        return f"{s:.0f}%"
    return "F"


main()