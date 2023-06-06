

groceryList = []

def main():
    
    userInput = int(input("""Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: """))

    if userInput == 1:
        groceryList.append(input("What will be added?: "))

    elif userInput == 2:
        num = int(input(f"There are {len(groceryList)} items in the list."
              "Which item is deleted?: "))
        
        if num > len(groceryList) - 1:
            print("Incorrect selection.")
        
        else:
            groceryList.pop(num)


    elif userInput == 3:
        print("The following items remain in the list:")
        for i in groceryList:
            print(i)
        quit()
    
    else:
        print("Incorrect selection.")

while True:  
    main()