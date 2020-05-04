import random
from keylist import KEYLIST
from scalelist import SCALELIST

def main():
    key   = random.choice(KEYLIST)
    scale = random.choice(SCALELIST)

    print(key, scale)

main()
