size = int(input("Enter the no of items you want to add in Dictonary: "))
Dict = dict()
for i in range(size):
    key = input("Enter the key for item " + str(i + 1) + " in dictonary: ")
    value = int(input("Enter the value for item " + str(i + 1) + " in dictonary: "))
    Dict[key] = value
valueList = list(Dict.values())
valueList.sort()
print("The second largest value in the Dictonary is", valueList.sort()[-2])
