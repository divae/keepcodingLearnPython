ASCII_BLANK = 32

text = " Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,"\
"totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo."\
"Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit,"\
"sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt."\
"Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit,"\
"sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem."\
"Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur?"\
"Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? "

def number_characters(text):
    count = 0
    for character in text:
        count += 1
    return count

def is_ascii_blank(character):
    return ord(character) == ASCII_BLANK

def add_word_to_list(words,word):
    words.append(word)
    return words

def init_string(word):
    return ''

def add_character_to_word(character,word):
    if not is_ascii_blank(character):
        word += character
    return word

def number_words(text):
    return len(list_words(text))

def empty(word):
    _empty = 0
    return len(word) != _empty
    
def list_words(text):
    word = ''
    words = []
    
    for character in text:
        if is_ascii_blank(character) and empty(word):
            add_word_to_list(words,word)
            word = init_string(word)
        else:
            word = add_character_to_word(character,word)
               
    add_word_to_list(words,word)
    return words


print("total characters: ", len(text))
print("number of words : ", number_words(text))
print("list of words : ", list_words(text))

            