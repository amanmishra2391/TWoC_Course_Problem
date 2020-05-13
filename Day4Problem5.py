noOfVotes = int(input("Enter the no of votes: "))
Votes = []
for i in range(noOfVotes):
    Votes.append(input("Enter the name of the Candidate to cast the Vote: "))
vote = set(Votes)
Vote = list()
for name in Votes:
    Vote.append((name, Votes.count(name)))  
Vote.sort(key = lambda x : x[0], reverse = True )
Vote.sort(key = lambda x : x[1])
print("The name of the candidate who won the election is",Vote[-1][0])
