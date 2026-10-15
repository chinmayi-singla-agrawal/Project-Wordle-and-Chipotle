# Author   : Chinmayi Singla Agrawal
# Email    : csinglaagraw@umass.edu
# Spire ID : 35726631



def get_guess():
    a = input("What word is this: ")
    return a.upper()

def print_word(x):
    print(x[0], x[1], x[2], x[3], x[4])

def exact_match_compare(solution, guess):
    result = ''
    i = 0
    while i<= 4:
        if solution[i]==guess[i]:
            result += '🟢' 
        else:
            result += '🔴'
        i += 1
    return result


def one_turn(solution):
    word = get_guess()
    print_word(word)
    print(exact_match_compare(solution, word))
    if solution == word:
        print("Congratulations!")
        exit()


import random
def make_solution():
    solution = random.choice(["WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE", "ABOUT", "FIRST", "COULD", "AFTER"])
    return solution 

soln = make_solution()
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
print(f"Word was \"{soln}\", better luck next time.")









