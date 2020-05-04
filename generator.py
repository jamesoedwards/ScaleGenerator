import random
from keylist import KEYLIST
from scalelist import SCALELIST
from scaleguide import SCALEMAP

def generate():
    key   = random.choice(KEYLIST)
    scale = random.choice(SCALELIST)

    return key, scale

def getScaleGuide(scale):
    return SCALEMAP[scale]

def main():
    print("\n>>> ScaleGenerator by James Edwards\n")
    print("--- press h for help --")
    print("--- press q to quit ---\n\n")

    cont = True
    while cont:
        key, scale = generate()
        print(">>>", key, scale)
        uInpt = input()
        if uInpt == "h" or uInpt == "H":
            guide = getScaleGuide(scale)
            print(guide)
            uInpt = input()

        if uInpt == "q" or uInpt == "Q":
            cont = False
    # End: while
    
    return

main()
