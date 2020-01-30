import random
import hangman_func

wordlist=["cat","dog","horse","monkey","eel","iguana","lizard"]
hangman(wordlist[random.randint(0,len(wordlist)-1)])
