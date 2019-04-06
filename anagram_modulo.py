import timeit
import anagram

first_word = 'amor'
second_word = 'roma'

response_anamgram = anagram.is_anagram(first_word,second_word)
anagram.show_response_anamgram(response_anamgram)

t = timeit.Timer("anagram.is_anagram('amor','roma')","from __main__ import anagram")
timeAnagram = t.timeit()
print("simple:{}".format(timeAnagram))



