fibonacci = set()
array = list(map(int,input("Enter the element in array seprate by space: ").strip().split(" ")))
Max = sum(array)
a = 0
b = 1
while a <= Max:
    fibonacci.add(a)
    c = a + b
    a = b
    b = c
Sum = 0
for x in array:
    if x in fibonacci:
        Sum += x
if Sum in fibonacci:
    print("The sum of fibonacci elements in the array is a Fibonacci number.")
else:
    print("The sum of fibonacci elements in the array is not a Fibonacci number.")
