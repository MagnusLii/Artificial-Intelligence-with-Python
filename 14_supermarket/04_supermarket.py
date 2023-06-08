
prices = [10,14,22,33,44,13,22,55,66,77]
totalprice = 0

def shopping():
    global totalprice
    while True:
        userInput = int(input("Please select product (1-10) 0 to Quit: "))

        if userInput == 0:
            return totalprice
        else:
            print(f"Product:  {userInput} Price:  {prices[userInput - 1]}")
            totalprice += prices[userInput - 1]


print("""Supermarket
===========""")
print(f"Total: {shopping()}")
change = int(input("Payment: "))
print(f"Change: {change - totalprice}")

