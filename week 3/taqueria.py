def main():
    
    food = order()

def order():
    menu  = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00 }
    total=0

    while True:
        try:
            food_ordered = input("Item: ").title()     
        except EOFError:
            break

        if food_ordered not in menu:
            continue
        
        total += menu.get(food_ordered)
        print(f"Total: ${total:.2f}")

    return total

main()