äIn the second exercise the idea is to create a small grocery shopping list with the list datastructure. In short, create a program that allows the user to (1) add products to the list, (2) remove items and (3) print the list and quit.

 

If the user adds something to the list, the program asks "What will be added?: " and saves it as the last item in the list. If the user decides to remove something, the program informs the user about how many items there are on the list (There are [number] items in the list.") and prompts the user for the removed item ("Which item is deleted?: "). If the user selects 0, the first item is removed. When the user quits, the final list is printed for the user "The following items remain in the list:" followed by the remaining items one per line. If the user selects anything outside the options, including when deleting items, the program responds "Incorrect selection.". When the program works correctly it prints out the following:





		
>>> 
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: 1
What will be added?: Apples
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: 1
What will be added?: Beer
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: 1
What will be added?: Carrots
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: 2
There are 3 items in the list.
Which item is deleted?: 3
Incorrect selection.
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: 2
There are 3 items in the list.
Which item is deleted?: 2
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: 2
There are 2 items in the list.
Which item is deleted?: 0
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: 4
Incorrect selection.
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: 3
The following items remain in the list:
Beer
>>>  

