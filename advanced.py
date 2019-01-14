# ┌ is 9484
# └ is 9492
# ┘ is 9496
# ┐ is 9488
# | is 124

def main():
    while True:
        try:
            w = int(input("What is the width? (minimum 2) "))
            if w < 2:
                print("Input must be an INTEGER greater than 2, please try again.")
                continue
            break
        except ValueError:
            print("Input must be an INTEGER greater than 2, please try again.") 
    while True:
        try:
            h = int(input("What is the height? (minimum 2) "))
            if h < 2:
                print("Input must be an INTEGER greater than 2, please try again.")
                continue
            break
        except ValueError:
            print("Input must be an INTEGER greater than 2, please try again.")

    top = chr(9484)
    bottom = chr(9492)
    row = chr(124)
    for i in range(0,w-2):
        top = top + "-"
        bottom = bottom + "-"
        row = row + " "
    top = top + chr(9488)
    bottom = bottom + chr(9496)
    row = row + chr(124)
    print(top)
    for i in range(0,h-2):
        print(row)
    print(bottom)
    
    while True:
        finished = input("Cool shape!\nDo you want to draw a new one?\nPlease enter yes or no: ")
        if not ((finished=="yes") or (finished=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if finished == "yes":
        main()
    else:
        print("Cheers, bye!")


print("Welcome to the program.\nThis program allows the creation of squares and rectangles!")    
main()
