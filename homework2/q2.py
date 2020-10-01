from nltk.book import text6
import re

words = (word.lower() for word in set(text6))
words = list(words)
print('length of words>', len(words))   

pattern1 = 'ize$'
pattern2 = '[z]'
pattern3 = 'pt'
found_words = [word for word in words if re.search(pattern1, word)
               or re.search(pattern2, word) or re.search(pattern3, word)]
print('length of found_words>', len(found_words))
print(found_words)
