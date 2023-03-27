import sys
import time

alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
num_list = range(1, 20000)
def string_q():
    global string
    for g in """Please type a word or string...
""":
        sys.stdout.write(g)
        sys.stdout.flush()
        time.sleep(.05)
    str_q = input("->")
    string = list(str_q)
    for n in f"""There are {len(string)} characters in {str_q} please select a number from 1 to {len(string)}...
""":
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(.05)
    character_q()

def character_q():
    character = int(input("->"))
    print(type(character))
    character_type(string, character)

def apology():
    for c in """There does not seem to be that many characters in your word/phrase...
""":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.05)
    character_q()

def character_type(word, char):
    word = string
    char = character
    spec_char = string[char]
    string_cnt = len(string)
    print(f"our string length is {string_cnt}, our variable type is {type(string_cnt)}")
    for char in word:
        print(f"our character is {type(char)}")
        if char > string_cnt:
            apology()
        elif spec_char in num_list:
            for u in f"""The character {string(char)}is a number...""":
                sys.stdout.write(u)
                sys.stdout.flush()
                time.sleep(.05)
            string_q()
        elif spec_char in alpha_list:
            for i in f"The character {string(char)} is a letter...""":
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.05)
            string_q()
        else:
            for a in f"""The character {string(char)} is unknown...""":
                sys.stdout.write(a)
                sys.stdout.flush()
                time.sleep(.05)
            string_q()

string_q()