import sys
from random import randint
from collections import Counter


def zero_incorrect(): return '\n'


def first_incorrect(): return (
        """

        |
        |
        |
        |
        |
        """
)


def second_incorrect(): return (
        """
        ~~~~~
        |
        |
        |
        |
        |
        """
)


def third_incorrect(): return (
        """
        ~~~~~
        |   |
        |
        |
        |
        |
        """
)


def fourth_incorrect(): return (
        """
        ~~~~~
        |   |   
        |   0   
        |
        |
        |
    ===============
        """
)


def fifth_incorrect(): return (
        """
        ~~~~~
        |   | 
        |   0   
        |  -%-  
        |
        |
    ===============
        """
)


def sixth_incorrect(): return (
        """
        ~~~~~
        |   |   
        |   0   
        |  -%-  
        |  /   
        |
    ===============
        """
)


def seventh_incorrect(): return (
        """
        -----
        |   |   
        |   0   
        |  -%-  
        |  / \  
    ===============
        """
)


def init() -> None:
    """ The init function starts the games main loop"""
    while True:
        sys.stdout.write("Enter 'y' to play or 'q' to quit:\n")
        play = sys.stdin.readline().lower().strip()

        if play == "y":
            secret_word = words[randint(0, len(words))]
            play_game(secret_word)
        elif play == "q":
            sys.stdout.write("Thanks for playing!\n")
            return
        else:
            sys.stderr.write("\nError:\n")
            return


def play_game(word: str) -> None:
    """ The play_game function initializes the game variables, and starts the current game loop

    Args:
        word (str): The word the player must guess, chosen randomly from a list of programming related words
    """
    wrong_list = []
    answer = []
    lives = 7
    correct_guess = 0
    score = 0
    while lives > 0:
        if check_if_game_won(len(answer), len(remove_duplicates(word))):
                return

        result, letter = guess(word)
        if result:
            correct_guess += 1
            score += 10
            answer.append(letter)
            display(lives, score, word, answer, wrong_list)
        else:
            lives -= 1
            wrong_list.append(letter)
            score -= 10
            display(lives, score, word, answer, wrong_list)

    sys.stdout.write(f"\nThe word was: {word}. Play again.\n\n")


def guess(word: str) -> tuple:
    """ The guess function takes a guess letter from the player and checks if it is in the word

    Args:
        word (str): The word the player is trying to guess

    Returns:
        tuple(bool, str): a tuple containing the result of the check if the letter is in the word and the letter the player guessed
    """
    sys.stdout.write("\nChoose a letter: ")
    letter = sys.stdin.readline().lower().strip()
    result = False
    if letter in word:
        result = True
    return result, letter


def display(lives, score, word, answer, wrong_list) -> None:
    """ The display function controls the state of the art cli gui

    Args:
        lives (int): the amount of lives remaining
        score (int): the current score
        word (str): the word to be guessed by the player
        answer (list): a list containing the correct player guesses
        wrong_list (list): a list containing wrong player guesses
    """
    sys.stdout.write(gui[lives]()) 
    sys.stdout.write(str(score) + "\n")
    sys.stdout.write("**********************\n")
    for letter in word:
        if letter in answer:
            sys.stdout.write(f"{letter}")
        else:
            sys.stdout.write("-")
    sys.stdout.write("\n**********************\n")
    sys.stdout.write(f"\nCorrect guesses: {', '.join(answer)}\n")
    sys.stdout.write(f"\nIncorrect guesses: {', '.join(wrong_list)}\n")


def check_if_game_won(answer_length, word_length) -> bool:
    """ This function is used check if the game has been won

    Args:
        answer_length (int): the length of the answer list
        word_length (int): the length of the word the play has to guess

    Returns:
        bool: true if game is won otherwise false
    """
    if answer_length == word_length:
        sys.stdout.write("""
            Art by Joan Stark
                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
    *
        *
        """)
        sys.stdout.write("\n\t\tCongratulations You've Won!!!\n\n")
        return True
    else:
        return False


def remove_duplicates(word) -> str:
    """ Removes duplicate letters in word

    Args:
        word (str): the word the player has to guess

    Returns:
        str: the argument word with no duplicates
    """
    temp: Counter = Counter(word)
    for letter, count in temp.items():
        if count > 1:
            temp[letter] = 1
    return ''.join(temp)


def main():
    sys.stdout.write("Welcome to my programming themed hangman game...\n")
    init()


gui = {
    # The functions for the display
    7: zero_incorrect,
    6: first_incorrect,
    5: second_incorrect,
    4: third_incorrect,
    3: fourth_incorrect,
    2: fifth_incorrect,
    1: sixth_incorrect,
    0: seventh_incorrect
}


words = ["hello", "world", "purple", "garbage", "bugs", "function", "query", "javascript", "python", "recursion", "rust", "arduino", "linear", "graph", "complexity", "space", "time", "algorithm", "post", "schema", "class", "object", "method", "attribute", "queue", "stack"]

                
if __name__ == '__main__':
    main()