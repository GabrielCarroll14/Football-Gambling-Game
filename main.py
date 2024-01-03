# Import random
import random

# Create the balance variable
balance = 100

# Intro
print ("Welcome to football gambling game! Bet on teams to win!")

# Create the main loop
while True:
    
    # Create a sub loop for generating the teams
    while True:
        
        # Put the random teams into two variables
        team1 = random.choice(("Arsenal", "Aston Villa", "Barnsley", "Birmingham City", "Blackburn Rovers", "Blackpool", "Bolton Wanderers", "Bradford City", "Burnley", "Cardiff City", "Manchester City", "Manchester United",))          
        team2 = random.choice(("Arsenal", "Aston Villa", "Barnsley", "Birmingham City", "Blackburn Rovers", "Blackpool", "Bolton Wanderers", "Bradford City", "Burnley", "Cardiff City", "Manchester City", "Manchester United",))
        
        # This is to prevent errors when the teams could be the same. so instead just carrying on if the teams are the same, it will only break out of the loop if the teams are different.
        if team1 != team2:
            break

    # Ask the user which team they would like to bet on
    team = int(input("What team would you like to bet on? " + team1 + ", or " + team2 + "? (1, 2) ")) 
    
    # Create a sub loop while asking the user how much they would like to bet
    while True:
        # Ask the user how mucjh they would like to bet
        amount = int(input("How much would you like to bet? £"))
        
        # If the user bets over £100 the loop will continue and the will be reprompted
        if amount > 100:
            print ("Invalid bet amount: Max bet of £100. ")
            
        # If the amount they would like to bet is under £100 the loop will break
        elif amount <= 100:
            break
    
    # Randomise the teams scores
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
