string = input("Enter the string: ")
letters = 0
for x in set(string):
    letters += string.count(x) % 2
if letters > 0:
    letters -= 1
print("The input string will form a pallindrome string from the letters after removing",letters,"which are not in pairs.")
