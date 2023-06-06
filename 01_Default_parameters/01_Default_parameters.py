
def main():
    userInput = input("Write something (quit ends): ")
    tester(userInput)


def tester(givenstring = "Too short"):
    if givenstring == "quit":
        quit()

    elif len(givenstring) < 10:
        print("Too short")

    else:
        print(givenstring)

    main()


main()
