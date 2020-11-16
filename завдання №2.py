a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Whether the numbers belong to the intervals?\n 1<=, 2>= and 3<, 7> ")

if 1 <= a <=2 or 3< a <7:
    print("\n---------------\nfirst number belong")
else:
    print("\n---------------\nfirst number does not belong to the gap")

if 1 <= b <=2 or 3< b <7:
    print("\n---------------\nsecond number belong")
else:
    print("\n---------------\nsecond number does not belong to the gap")