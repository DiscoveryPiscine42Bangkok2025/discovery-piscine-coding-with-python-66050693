import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    result = "".join([ch for ch in text if ch == "z"])
    if result:
        print(result)
    else:
        print("none")