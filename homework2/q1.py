from nltk.book import text5
from nltk.corpus import words
from nltk import FreqDist

FOUND_WORD_LENGTH = 4
word_set = set(text5)
chat_words = (word.lower() for word in word_set if len(word) is FOUND_WORD_LENGTH and word.isalpha())
chat_words = list(chat_words)
print('================')
print('length of chat_words>', len(chat_words))

all_words = words.words()
all_words_contains_chat_words = [word for word in all_words if word in chat_words]
freq = FreqDist(all_words_contains_chat_words)
print('length of frequency>', len(freq))
for word in list(freq):
    print(word, '=', freq[word], end=', ')
print('\n================')