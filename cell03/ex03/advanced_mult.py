import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:
        print("Table de {}:".format(i), end=" ")
        
        j = 0
        while j <= 10:
            print("{}".format(i * j), end="")
            if j < 10:
                print(" ", end="")
            j += 1
        
        print()
        i += 1
