def have_same_number_words(first_word,second_word):
    return len(first_word) == len(second_word)   

def not_repeated(__tupla__,value):
    return True if number_of_coincidences(__tupla__,value) == 1 else False

def number_of_coincidences(__tupla__,value):
    return __tupla__.count(value)

def exist(__tupla__,value):
    return True if number_of_coincidences(__tupla__,value) == 1 else False

def is_anagram(first_word,second_word):    
    is_anagram = False
    
    if have_same_number_words(first_word,second_word):
        first_letters = tuple(first_word)
        second_letters = tuple(second_word)
                
        for letter in first_letters:
            if not_repeated(first_letters,letter) and exist(second_letters,letter) :
                is_anagram = True
            else:
                return False
        
    return is_anagram

def show_response_anamgram(response_anamgram):
    if response_anamgram:
        print("Correct! Is anagram")
    else:
        print("Ups! Not Is anagram")
        


