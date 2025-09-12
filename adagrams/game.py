from random import randint
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
def draw_letters():
    # turns the dictionary LETTER_POOL into a letters list 
    letter_deck = []
    letter_bank = []
    for letter, freq in LETTER_POOL.items():
        for i in range(freq):
            letter_deck.append(letter)
    
    for i in range(10):
        index = randint(0,len(letter_deck)-1)
        letter_bank.append(letter_deck[index])
        letter_deck.pop(index)

    return letter_bank
 

def uses_available_letters(word, letter_bank):
    filtered = []
    letter_bank_count = {}
    # Count letters in the bank, store in a dict
    for letter in letter_bank:
        letter_bank_count[letter] = letter_bank_count.get(letter,0) + 1



    for letter in list(word.upper()):
        if letter_bank_count.get(letter,0) > 0:
            filtered.append(letter)  # Build filtered list and check availability
            letter_bank_count[letter] -= 1 # decrease count in dict only
        else:
            return False

   # Check if all letters were used
    if filtered == list(word.upper()):
        return True
    else:
        return False



    

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass