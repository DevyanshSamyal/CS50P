amount_due = 50
coins_collected = 0
valid_coin = [25, 10, 5]

while coins_collected < amount_due:
    print(f"Amount Due: {amount_due - coins_collected}")
    coin = int(input("Insert Coin: "))

    if coin not in valid_coin:
        continue

    coins_collected += coin

print(f"Change Owed: {coins_collected - amount_due}")