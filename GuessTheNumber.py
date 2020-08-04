# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

game_range = 100


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, game_range)
    
    global rem_guess 
    rem_guess = int(math.ceil(math.log(game_range + 1, 2)))
    
    print "New game. Range is from 0 to", game_range
    print "Number of remaining guesses is", rem_guess,"\n"
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global game_range
    game_range = 100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global game_range
    game_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global rem_guess
    rem_guess -= 1
    
    guess_num = int(guess)
    print "Guess was " + guess
    print "Number of remaining guesses is", rem_guess
 
    #Check if you guessed the correct number
    #Otherwise, only if you have remaining guesses it will tell if it is higher or lower
    #If there is no more guesses end the game
    
    if(guess_num == secret_number):
        print "Correct!\n"
        new_game()
    elif(rem_guess > 0):
        if(guess_num > secret_number):
            print "Lower!\n"
        elif(guess_num < secret_number):
            print "Higher!\n"
    else:
        print "You ran out of guesses.", "The number was", secret_number, "\n"
        new_game()

    
# create frame
frame = simplegui.create_frame("GuessTheNumber",300,300)


# register event handlers for control elements and start frame
button1 = frame.add_button("Range [0 - 100)",range100,200)
button2 = frame.add_button("Range [0 - 1000)",range1000,200)
textinput = frame.add_input("Guess",input_guess,200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
