# Import random
import random

# Create the balance variable
balance = 100

score = 0

# The self created user name
u_name = "" # This will be set by the user later in the game

# Create the update score function
def update_score():
    global score
    score = balance
    print ("New high score of " + str(score) + "! ")
    with open ("scores.txt", "a") as scores:
        scores.write (u_name + " | " + str(score) + "\n")

# Create a starting loop for asking the user for their username
while True:
    u_name = input ("Please enter a username. ")
    choice = input ("Are you shure you want your username to be " + u_name + "? (y, n)")
    if choice == "y":
        break
    if choice == "n":
        print ("Please reset your username. ")
    else:
        print ("Invalid answer: Please Retry")
    
# Intro
print ("Welcome to football gambling game! Bet on teams to win!")

# Create the main loop where the game is stored so when the loop has finished it will start again
while True:
    
    # Create a sub loop for generating the teams
    while True:
        # Put the random teams into two variables
        team1 = random.choice(("Arsenal", "Aston Villa", "Barnsley", "Birmingham City", "Blackburn Rovers", "Blackpool", "Bolton Wanderers", "Bradford City", "Burnley", "Cardiff City", "Manchester City", "Manchester United",))          
        team2 = random.choice(("Arsenal", "Aston Villa", "Barnsley", "Birmingham City", "Blackburn Rovers", "Blackpool", "Bolton Wanderers", "Bradford City", "Burnley", "Cardiff City", "Manchester City", "Manchester United",))
        # This is to prevent errors when the teams could be the same. so instead just carrying on if the teams are the same, it will only break out of the loop if the teams are different.
        if team1 != team2:
            break
        
    
    # Create a sub loop for asking the user what team they are going to bet on
    while True:
        # Ask the user which team they would like to bet on
        team = int(input("What team would you like to bet on? " + team1 + ", or " + team2 + "? (1, 2) "))
        # If team is equal to 1 break out of the loop
        if team == 1:
            break
        # If team is equal to 2 break out of the loop
        elif team == 2:
            break
        # If user responce is not one or two redo the loop
        else:
            ("Invalid Answer: Please retry. ")
    
    
    # Create a sub loop for asking the user how much they would like to bet
    while True:
        
        # Ask the user how much they would like to bet
        amount = int(input("How much would you like to bet? £"))
        
        # If the user bets over £100 the loop will continue and the will be reprompted
        if amount > 100:
            print ("Invalid bet amount: Max bet of £100. ")
        
        # If the user bets over the amount in their account the system will reprompt them
        elif amount >= balance:
            print ("You cannot bet over the amount in your balance, in your case £" +str(balance) + ". ")
        
        # If the amount they would like to bet is under £100 the loop will break
        elif amount <= 100:
            break
        
        else:
            print ("Invalid Answer: The amount must be an integer and less than £100. ")
     
    
    # Randomise the teams scores
    team1score =  random.randint(1, 10)
    team2score =  random.randint(1, 10)
    
    # If the user selected team one run this
    if team == 1:
        
        # This option is if the user has won
        if team1score > team2score:
            print ("You won! The score was, " + team1 + " " + str(team1score) + ", " + team2 + " " + str(team2score) + "! ")
            # Update the balance
            balance = balance + amount
            print ("Your balance is £" + str(balance) + ". ")
            if balance >= score:
                update_score()
            # If the user is bankrupt restart the game
            if balance < 1:
                print ("You are now bankrupt please restart the game. ")
                break
        
        # This option is if the user has lost 
        if team1score < team2score:
            print ("You lost! The score was, " + team1 + " " + str(team1score) + ", " + team2 + " " + str(team2score) + "! ")
            # Update the balance
            balance = balance - amount
            print ("Your balance is £" + str(balance) + ". ")
            # If the user is bankrupt restart the game
            if balance < 1:
                print ("You are now bankrupt please restart the game. ")
                break
    
    # If the user selected team two run this        
    if team == 2:
        
        # This option is if the user has lost
        if team1score > team2score:
            print ("You lost! The score was, " + team1 + " " + str(team1score) + ", " + team2 + " " + str(team2score) + "! ")
            # Update the balance
            balance = balance - amount
            print ("Your balance is £" + str(balance) + ". ")
            if balance >=  score:
                update_score()
            # If the user is bankrupt restart the game
            if balance < 1:
                print ("You are now bankrupt please restart the game. ")
                break
            
        # This option is if the user has won    
        if team1score < team2score:
            print ("You won! The score was, " + team1 + " " + str(team1score) + ", " + team2 + " " + str(team2score) + "! ")
            # Update the balance
            balance = balance + amount
            print ("Your balance is £" + str(balance) + ". ")
            if balance >= score :
                update_score()
            # If the user is bankrupt restart the game
            if balance < 1:
                print ("You are now bankrupt please restart the game. ")
                break
                
