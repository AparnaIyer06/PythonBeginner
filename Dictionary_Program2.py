#A dictionary containing the names of competition winners as keys and the number of wins as values
n=int(input("Enter the number of winners: "))
WinsDict=dict()
for i in range(1,n+1):
    name=input("Enter your name: ")
    no_of_wins=int(input("Enter the number of wins: "))
    WinsDict[name]=no_of_wins
for i,j in WinsDict.items():
    print("Name of the winner: ",i,"\n No of competitions won: ",j)
    
    
