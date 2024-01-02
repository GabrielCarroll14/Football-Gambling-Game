# Import random
import random

balance = 100

print ("Welcome to football gambling game! Bet on teams to win!")

while True:
    
    while True:
        team1 = random.choice(("Arsenal", "Aston Villa", "Barnsley", "Birmingham City", "Blackburn Rovers", "Blackpool", "Bolton Wanderers", "Bradford City", "Burnley", "Cardiff City", "Manchester City", "Manchester United",))          
        team2 = random.choice(("Arsenal", "Aston Villa", "Barnsley", "Birmingham City", "Blackburn Rovers", "Blackpool", "Bolton Wanderers", "Bradford City", "Burnley", "Cardiff City", "Manchester City", "Manchester United",))
        if team1 != team2:
            break

    team = int(input("What team would you like to bet on? " + team1 + ", or " + team2 + "? (1, 2) ")) 
    
    while True:
        amount = int(input("How much would you like to bet? £"))
        if amount > 100:
            print ("Invalid bet amount: Max bet of £100. ")
            
        elif amount <= 100:
            break
    
    team1score =  random.randint(1, 10)
    team2score =  random.randint(1, 10)
    
    if team == 1:
        
        if team1score > team2score:
            print ("You won! The score was, " + team1 + " " + str(team1score) + ", " + team2 + " " + str(team2score) + "! ")
            balance = balance + amount
            print ("Your balance is £" + str(balance) + ". ")
            
        if team1score < team2score:
            print ("You lost! The score was, " + team1 + " " + str(team1score) + ", " + team2 + " " + str(team2score) + "! ")
            balance = balance - amount
            print ("Your balance is £" + str(balance) + ". ")
            
    if team == 2:
        
        if team1score > team2score:
            print ("You lost! The score was, " + team1 + " " + str(team1score) + ", " + team2 + " " + str(team2score) + "! ")
            balance = balance - amount
            print ("Your balance is £" + str(balance) + ". ")
            
        if team1score < team2score:
            print ("You won! The score was, " + team1 + " " + str(team1score) + ", " + team2 + " " + str(team2score) + "! ")
            balance = balance + amount
            print ("Your balance is £" + str(balance) + ". ")
