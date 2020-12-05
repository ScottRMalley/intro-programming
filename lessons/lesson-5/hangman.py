# These are all the imports we will be using. You don't have to
# change any of the methods in util.py as they have been provided
import utils
import numpy as np


class HangmanGame:
    ###
    # This is the initialization function. It can be called by:
    #
    # hangman_game = HangmanGame(filename)
    #
    # where filename is the name of the word list file
    #
    # In this method we will need to create all necessary fields
    # in the HangmanGame object. These will be specific to each
    # instantiation of HangmanGame.
    ###
    def __init__(self, filename):
        # here we will need to use utils.getWordList to import the wordlist
        # replace [] with the appropriate function call.
        self.wordlist = []

        # we will also need fields for:
        # * self.selected_word   - represents the word selected from self.wordlist
        #                          for each round of hangman.
        # * self.num_wrong       - an int representing the number of wrong guesses
        #                          for this round of hangman.
        # * self.guessed_letters - a list representing how many letters have
        #                          been guessed this round.
        # * self.revealed        - a list representing which letters have been
        #                          revealed this round.
        # Include these below:

    ###
    # This is the method we will be using to print the current state of the hangman game.
    # the example should print something like this:
    #  +---+
    #  |   |
    #  O   |
    #      |
    #      |
    #      |
    #=========
    # _  e  _  _  _  e
    #
    # Guessed letters: [a e]
    #
    # In this scenario, the user has guessed the letters a and e, but only e had any places in
    # the selected word. Therefore print state should have just the head of the hangman showing.
    # utils.HANGMAN_ART[index] will give you the correct string to print for each index 0 to 6.
    # Note that the entire hangman is shown after index = 6.
    #
    # Below the hangman art, we will need to give an indication of how many letters are in the
    # selected_word and how many of those letters have been guessed correctly. So for a selected
    # word with 5 letters (eg. games), and none guessed, the printed line would be:
    # _ _ _ _ _
    #
    # if one letter has been guessed, (eg. a) the printed line would look like this:
    # _ a _ _ _
    #
    # We can use the class field self.revealed which will contain a list of correctly guessed
    # letters.
    #
    # Be sure to include the guessed letters  at the end so the player knows which letters have
    # already been guessed.
    ###
    def print_hangman_state(self):
        # write code here

    ###
    # For this method, we want to take a guessed_letter and update the hangman state.
    #
    # If the letter is wrong:
    #   - self.num_wrong should increase by 1
    # If the letter is correct:
    #   - the letter should be added to the list self.revealed so that it can be shown
    # If the letter has already been guessed:
    #   - we should print a warning "letter has already been guessed" and do nothing else
    ###
    def guess(self, guessed_letter):
       # write code here

    ###
    # This is where we bring everything together. A basic round of hangman involves the
    # player guessing a letter, the game updates the state, and then prints out the new state.
    #
    # Remember to start a new game by setting all the class fields back to their initialized values
    # eg. self.guessed_letters = []
    #
    # Also make sure to print the state before any guessed letters are input, as the player needs to
    # know how many blank spaces they are guessing for.
    #
    # The game should stop after either the hang man is hung, or all letters have been revealed
    ###
    def play_new_game(self):
        # Reset all field values. I have set a game_over variable for you here, but you
        # will need to reset all other object fields yourself.
        game_over = False

        # While the game isn't over, enter guesses and update state
        while not game_over:
            # print current state

            # get new guess (you can use input(prompt) to retrieve the guess from the command line)

            # update state from guess

            # recalculate game_over

        # print end state and give the word


if __name__ == '__main__':
    # this part has been done for you. If the above is written correctly, running this program should
    # let you play a game of hangman
    hangman = HangmanGame('wordlist.txt')

    while input('Start new game? (yes or no)').lower() == 'yes':
        hangman.play_new_game()




