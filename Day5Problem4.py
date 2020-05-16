size =  int(input("Enter the number of items you want to enter: "))
List = []
for i in range(size):
    weight = int(input("Enter the weight for item number " + str(i + 1) + ": "))
    value = int(input("Enter the value for item number " + str(i + 1) + ": "))
    List.append((weight,value))
print(List)