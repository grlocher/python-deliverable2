print("Welcome to the GC Fruit Market!")
name = input("What is your name? ")

print(f"Welcome, {name}! Which fruit would you like to buy?")

fruits = ['Apple', 'Grape', 'Orange']
prices = [2, 1, 3]
cart = []
subtotal = 0
sales_tax = 0.05

while True:
    for i in range(len(fruits)):
        print(f"{i + 1}) {fruits[i]} ${prices[i]}")
    purchase = int(input())
    if purchase == 1:
        print(f"You bought 1 {fruits[0]} at ${prices[0]}.")
        cart.append((fruits[purchase-1], prices[purchase-1]))
        additional_purchase = input("Would you like to buy another piece of fruit? y/n ")
        if additional_purchase != "y":
            break
    elif purchase == 2:
        print(f"You bought 1 {fruits[1]} at ${prices[1]}.")
        cart.append((fruits[purchase-1], prices[purchase-1]))
        additional_purchase = input("Would you like to buy another piece of fruit? y/n ")
        if additional_purchase != "y":
            break
    elif purchase == 3:
        print(f"You bought 1 {fruits[2]} at ${prices[2]}.")
        cart.append((fruits[purchase-1], prices[purchase-1]))
        additional_purchase = input("Would you like to buy another piece of fruit? y/n ")
        if additional_purchase != "y":
            break
    else:
        break

print(f"Order for {name}:")

for fruits, prices in set(cart):
    quantity = cart.count((fruits, prices))
    subtotal += quantity * prices
    print(f"{quantity} {fruits}(s) at ${prices} apiece")

tax = subtotal * sales_tax
total = subtotal + tax

print()
print(f"Subtotal: ${subtotal}")
print(f"5% Tax: ${tax}")
print(f"Total: ${total}")