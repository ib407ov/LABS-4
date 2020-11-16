import math

A = float(input("Enter A: "))
C = float(input("Enter C: "))
N = float(input("Enter N: "))

if A == C and C == N :
    Rezult = math.cos(A + C + N)
elif A < C and C == N :
    Rezult = math.cos(A * C * N)
elif A < C and C < N :
    Rezult = math.cos((A + C) * N)
else:
    Rezult = 0

print("Rezult = {0}".format(Rezult))