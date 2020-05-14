def Ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return Ackermann(m - 1, 1)
    return Ackermann(m - 1, Ackermann(m, n - 1))
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))
print("The result of Ackermann Function is", Ackermann(m,n))
