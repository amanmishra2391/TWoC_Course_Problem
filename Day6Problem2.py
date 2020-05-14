size = int(input("Enter the number of strings you want to add: "))
Max = 0
List = []
for i in range(size):
    string = input("Enter the element in List of 0's and 1's: ")
    List.append(string)
    if Max < len(string):
        Max = len(string)
for i in range(size):
    if len(List[i]) < Max:
        List[i] = "0" * (Max - len(List[i])) + List[i]
List.sort()
print("After sorting the list in non-decreasing order the list becomes:",", ".join(List))
