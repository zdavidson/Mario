#Mario Pyramid Builder

print(
    "\nHello! Are you ready to play Mario? \nBefore we can play, we have to build one of our obstacles. \nLet's build a pyramid.\n" )

Height = int(input("In meters, how tall would you like your pyramid to be? "))
print("Great, thank you! \n\nYour pyramid will be {m} meters tall.".format(m=Height))

def pyramids():
    column_count = 0
    while column_count <= Height:
        print((" "*(Height*2-(Height + column_count))) + ("#"*column_count) + "  " + ("#"*column_count))
        column_count += 1
    return

pyramids()

print("\nThat's a great pyramid!\n")