import random
from words import words

def validating_word(words):
    word = random.choice(words) #chooses random word from the list words
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

def hangman():
    word = validating_word(words).upper()
    word_letters = set(word.upper()) #stores all letters in the word
    used_letters = set() #stores letters used by the users
    letter_list = []
    tries = 6 #no of tries that user gets

    while tries > 0: #ends if no tires are left
        letter_list = [letter if letter in used_letters else '-' for letter in word]

        if len(word_letters) == 0: #ends the game if the correct word is guessed
            print(f"\n\n{word} IS CORRECT.\nCongratulations. You've won. Lets play again.")
            again()
            
        

        print("\nYour current word: ", ' '.join(letter_list))
        print("Tries left", tries)
        print(hangman_display(tries))
        guess = input("\n\nGuess a letter in the word: ").upper()

        if guess in used_letters: #if letter is already used.
                tries -=1
                print("REPEATED GUESS. Try Again.")

        elif guess in word_letters and guess.isalpha(): #the guess is correct
                print(f"THAT IS A RIGHT LETTER.")
                word_letters.remove(guess)

        else: #the guess is wrong
            tries -=1
            print("THAT IS WRONG. Try Again")
        used_letters.add(guess)
        # print("Your used letters are: ", ' '.join(used_letters))

        
    else:
        print("\n\nyour tries are completed.")
        print(hangman_display(tries))
        print("the word was:", word, "\nYOU'VE LOST")
        again()



def hangman_display(tries):
    stages = [  # final state: head, torso, both arms, and both legs
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """,
    # head, torso, both arms, and one leg
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
       -
    """,
    # head, torso, and both arms
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    """,
    # head, torso, and one arm
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |     
       -
    """,
    # head and torso
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |     
       -
    """,
    # head
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    """,
    # initial empty state
    """
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    """]
    return stages[tries]

def again():
    if input("\n\nDo you want to play more? (Y/N): ").upper() == 'Y':
        print("""
    -------------------------------
    THE HANGMAN GAME BEGINS AGAIN
    -------------------------------
    """)
        print("You get 6 tries to complete this hangman challenge")
        hangman()
    else:
        print("Hope to see you soon.")
        exit()


#The program starts from here.
print("""
-------------------------
 THE HANGMAN GAME BEGINS 
-------------------------
""")
print("You get 6 tries to complete this hangman challenge")
hangman()




