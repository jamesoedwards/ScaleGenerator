import random
from keylist import KEYLIST
from scalelist import SCALELIST

def generate():
    key   = random.choice(KEYLIST)
    scale = random.choice(SCALELIST)

    ret = key + " " + scale
    return ret

def main():
    print("\n>>> ScaleGenerator by James Edwards\n")
    print("--- press q to quit ---\n\n")

    cont = True
    while cont:
        scale = generate()
        print(">>>", scale)
        uInpt = input()
        if uInpt == "q" or uInpt == "Q":
            cont = False
    # End: while
    
    return

main()
