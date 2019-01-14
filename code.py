# Python program for drawing a square of size w by h determined by the user
# ┌ is 9484
# └ is 9492
# ┘ is 9496
# ┐ is 9488
# | is 124

def makeSquare(w,h):
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

wid = int(input("What is the width? (minimum 2) "))
hei = int(input("What is the height? (minimum 2) "))

makeSquare(wid,hei)
