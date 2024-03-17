import random
print("Welcome to the hangman game")
HANGMAN_PICS = ['''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

wordslist1 = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
wordslist2 ='apple banana orange grape pineapple watermelon kiwi strawberry blueberry raspberry blackberry peach pear plum mango papaya lychee cherry apricot fig coconut lemon lime avocado grapefruit pomegranate cranberry tangerine nectarine passionfruit guava elderberry kiwifruit dragonfruit persimmon starfruit cantaloupe honeydew mulberry'.split()
wordslist3='football basketball volleyball cricket rugby tennis golf baseball hockey swimming cycling skiing snowboarding surfing skating boxing wrestling athletics gymnastics badminton squash tabletennis archery shooting sailing rowing canoeing kayaking diving triathlon fencing handball judo karate taekwondo muaythai kickboxing polo horsebackriding pentathlon lacrosse cricket croquet rugby'.split()
wordslist4='red orange yellow green blue indigo violet cyan magenta turquoise maroon olive teal navy lavender periwinkle peach coral crimson magenta turquoise fuchsia chartreuse indigo sapphire emerald amethyst ruby amber topaz saffron ivory beige taupe khaki plum orchid mauve cyan teal auburn'.split()
wordslist5='elephant banana guitar mountain candle sunshine ocean laughter butterfly rainbow happiness adventure chocolate starlight firefly whisper moonlight waterfall serendipity blossom melody laughter sunshine laughter butterfly hummingbird rainbow freedom happiness tranquil whisper ocean firefly serendipity chocolate mountain laughter blossom moonlight butterfly waterfall elephant banana guitar starlight adventure butterfly rainbow'.split()


print("Choose your category: \n Animals-type 1 \n Fruits-type 2 \n Sports-type 3 \n Colours-type 4 \n Random-type 5")
a=int(input("enter you category:"))

#for different categories 
if(a==1):
    def getRandomWord(wordList1):
        wordIndex1 = random.randint(0, len(wordList1) - 1)
        return wordList1[wordIndex1]

elif(a==2):
    def getRandomWord(wordList2):
   
        wordIndex2 = random.randint(0, len(wordList2) - 1)
        return wordList2[wordIndex2]
elif(a==3):
    def getRandomWord(wordList3):
   
        wordIndex3 = random.randint(0, len(wordList3) - 1)
        return wordList3[wordIndex3]

elif(a==4):
    def getRandomWord(wordList4):
   
        wordIndex4 = random.randint(0, len(wordList4) - 1)
        return wordList4[wordIndex4]
else:
    def getRandomWord(wordList5):
   
        wordIndex5 = random.randint(0, len(wordList5) - 1)
        return wordList5[wordIndex5]




def displayBoard(missedLetters, correctLetters, secretWord):
    print()
    print(HANGMAN_PICS[len(missedLetters)])

    print()
    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')

    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    # Display the secret word with spaces between the letters:
    for letter in blanks:
        print(letter, end =' ')
    print()

def getGuess(alreadyGuessed):
    """
    Returns the letter the player entered.
    Ensures the player enters a single letter and nothing else.
    """
    while True:
        print('Please guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Only a single letter is allowed.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter from the alphabet.')
        else:
            return guess

def playAgain():
    """
    Returns True if the player wants to play again, False otherwise.
    """
    print('Would you like to play again? (y)es or (n)o')
    return input().lower().startswith('y')

print('|YOUR MAN IS HANGED|')
missedLetters = ''
correctLetters = ''

if(a==1):
    secretWord = getRandomWord(wordslist1)
elif(a==2):
    secretWord = getRandomWord(wordslist2)
elif(a==3):
    secretWord = getRandomWord(wordslist3)
elif(a==4):
    secretWord = getRandomWord(wordslist4)
else:
    secretWord = getRandomWord(wordslist5)

gameIsDone = False

# Now for the game itself:
while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # Let the player enter a letter:
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check to see if the player has won:
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('You guessed it!')
            print('The secret word is "' + secretWord + '"! You win!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if the player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
    # If the game is done, ask the player to try again.
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            if(a==1):
                secretWord = getRandomWord(wordslist1)
            elif(a==2):
                secretWord = getRandomWord(wordslist2)
            elif(a==3):
                secretWord = getRandomWord(wordslist3)
            elif(a==4):
                secretWord = getRandomWord(wordslist4)
            else:
                secretWord = getRandomWord(wordslist5)
    
        else:
            break
