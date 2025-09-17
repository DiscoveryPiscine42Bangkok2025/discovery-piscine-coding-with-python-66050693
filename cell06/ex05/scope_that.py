def add_one(n):
    n = n + 1
    print("Inside add_one:", n)

x = 5
print("Before calling add_one:", x)

add_one(x)

print("After calling add_one:", x)