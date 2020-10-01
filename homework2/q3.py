from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk import FreqDist
import random


def find_freq_top50(text):
    text_words = (word.lower() for word in set(text) if word.isalpha())
    text_words = list(text_words)

    english_stopwords = stopwords.words('english')
    text_words = [word for word in text_words if word not in english_stopwords]
    freq = FreqDist(text_words)
    return freq.most_common(50)


brown_categories = brown.categories()
random_category_index = random.randrange(0, len(brown_categories))
category = brown_categories[random_category_index]
print('category>', category)
my_text = list(brown.words(categories=category))
top50_from_my_text = find_freq_top50(my_text)
print(top50_from_my_text)
