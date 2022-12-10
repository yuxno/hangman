import random
from words import list_words


def get_word():
   word= random.choice(list_words)
   return word.upper()

def play(word):
    word_completion= "_" * len(word)
    guessed=False
    guessed_letter=[]
    guessed_words=[]
    tries=7
    print("let's play some HANGMAN!! \n")
    while not guessed and tries>0 :
        guess=input("give your guessed word or letter: ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letter:
                print("you already guessed this letter, try again !")
            elif guess not in word:
                print(guess ," is not in the word")
                tries -=1
                guessed_letter.append(guess)
            else:
                print("correct guess!")
                guessed_letter.append(guess)
                word_as_list=list(word_completion) #convert it as list
                indice=[i for i, letter in enumerate(word) if letter ==guess]
                for index in indice:
                    word_as_list[index]=guess
                word_completion="".join(word_as_list)
                if "_" not in word_completion:
                    guessed =True
        elif len(guess)==len(word) and guess.isalpha():
            if guess != word:
                print("wrong guess")
                tries -=1
                guessed_words.append(guess)
            else:
                guessed=True
                word_completion=word
        else:
            print("wrong choice!")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("congrats you guessed the word ", word)
    else:
        print("wrong guess, the word was: ", word)





def display_hangman(tries):
    stages=[ """
                 ---------
                 |    | 
                 |    o
                 |   \|/
                 |    |
                 |   / \
                 -
           """,
           """
                 ---------
                 |    | 
                 |    o
                 |   \|/
                 |    |
                 |   / 
                 -
           """,
           """
                 ---------
                 |    | 
                 |    o
                 |   \|/
                 |    |
                 |   
                 -
           """,
           """
                 ---------
                 |    | 
                 |    o
                 |   \|
                 |    |
                 |    
                 -
           """,
           """
                 ---------
                 |    | 
                 |    o
                 |    |
                 |    |
                 |    
                 -
           """,
           """
                 ---------
                 |    | 
                 |    o
                 |    |
                 |    
                 |    
                 -
           """,
           """
                 ---------
                 |    | 
                 |    o
                 |  
                 |    
                 |   
                 -
           """,
           """
                 ---------
                 |    | 
                 |    
                 |  
                 |   
                 |   
                 -
           """
           ]
    return stages[tries]

def main():
    word =get_word()
    play(word)
    while input("play again? Y/N \n").upper() == "Y":
        word= get_word()
        play(word)

if __name__ =="__main__":
    main()

        
  

    

