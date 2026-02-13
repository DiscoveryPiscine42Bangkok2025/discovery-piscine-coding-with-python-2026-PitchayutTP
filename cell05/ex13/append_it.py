import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    count = 0

    for word in args:
        if not word.endswith("ism"):
            print(word + "ism")
            count += 1

    if count == 0:
        print("none")