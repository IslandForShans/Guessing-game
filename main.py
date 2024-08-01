import random

userScore = 0
compScore = 0

def check_guess(playerguess, compNum):
    """Check the player's guess against the computer's number."""
    correct_position = sum(p == c for p, c in zip(playerguess, compNum))
    correct_number = sum(min(playerguess.count(x), compNum.count(x)) for x in set(playerguess)) - correct_position
    return correct_position, correct_number

def gameStart():
    global userScore, compScore, check
    
    number = range(1, 1001)
    compNum = random.choice(number)
    
    print("The computer has thought of a number between 1 and 1000.")
    print("You have 10 tries to guess the number right!")
    
    tries = 10
    
    while tries > 0:
        try:
            playerguess = int(input("Guess a number: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        correct_position, correct_number = check_guess(str(playerguess), str(compNum))
        
        if correct_position == len(str(compNum)):
            userScore += 1
            print(f"You've guessed the number with {tries} tries left! Well done!")
            print(f"Your Score: {userScore} | Computer Score: {compScore}")
            break
        else:
            tries -= 1
            if playerguess > compNum:
                print(f"Not quite! Numbers in the correct position: {correct_position}, correct numbers but wrong position: {correct_number}")
                print("Your number is GREATER!")
                print("Tries remaining:", tries)
            elif playerguess < compNum:
                print(f"Not quite! Numbers in the correct position: {correct_position}, correct numbers but wrong position: {correct_number}")
                print("Your number is LOWER!")
                print("Tries remaining:", tries)
    
    if tries == 0:
        compScore += 1
        print(f"You're out of guesses. The number was {compNum}. Try again!")
        print(f"Your Score: {userScore} | Computer Score: {compScore}")

# Start the game
gameStart()

while True:
    again = input("Play again? Y/N: ").strip().upper()
    
    if again == "Y":
        gameStart()
    elif again == "N":
        print("Thanks for playing!")
        print(f"Final Score: You: {userScore} | Computer: {compScore}")
        break
    else:
        print("Invalid input, please enter Y or N.")
