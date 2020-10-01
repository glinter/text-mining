import os
from bs4 import BeautifulSoup
import re
import collections
from nltk.stem import PorterStemmer


def find_freq_top50(text):
    freq = dict()
    for word in text:
        lower_word = word.lower()
        if lower_word in freq:
            freq[lower_word] += 1
        else:
            freq[lower_word] = 1
    sorted_freq = collections.OrderedDict(sorted(freq.items(), key=lambda freq_item: freq_item[1], reverse=True)[:50])
    return sorted_freq


def find_25percent_freq(text, freq):
    def percentage(target, total):
        return 100 * target / total
    word_count = 0
    word_freq_count = 0
    for word in freq:
        word_count += 1
        word_freq_count += text.count(word)
        calculated_percent = percentage(word_freq_count, len(text))
        if calculated_percent >= 25:
            return word_count
    return None


data_dir = './data/cranfieldDocs'
files_from_data_dir = os.listdir(data_dir)
raw_data_for_each_file = [dict() for i in range(0, len(files_from_data_dir))]
all_stemmed_text = []
count = 0
for file_name in files_from_data_dir:
    file = os.path.join(data_dir, file_name)
    doc = ''.join([line for line in open(file, 'r')])

    clean_text = BeautifulSoup(doc, 'lxml').text
    lower_text = clean_text.lower()

    lower_text = ''.join(i for i in lower_text if not i.isdigit())
    tokenized_text = re.sub('\\W+', ' ', lower_text).split()

    stop_words = [line.split()[0] for line in open('./data/stopwords_nltk.txt', 'r')]
    tokenized_text = [x for x in tokenized_text if x not in stop_words]

    stemmer = PorterStemmer()
    stemmed_text = [stemmer.stem(x) for x in tokenized_text]
    raw_data_for_each_file[count] = dict()
    raw_data_for_each_file[count]['total_word_count'] = len(stemmed_text)
    raw_data_for_each_file[count]['unique_word_count'] = len(set(stemmed_text))
    raw_data_for_each_file[count]['freq'] = find_freq_top50(stemmed_text)
    print('...{}> total_word_count: {}, unique_word_count: {}'.format(
        file_name,
        raw_data_for_each_file[count]['total_word_count'],
        raw_data_for_each_file[count]['unique_word_count']))
    all_stemmed_text += stemmed_text
    count += 1

print('=====')
print('> total_word_count in all documents:', len(all_stemmed_text))
print('> unique_word_count in all documents:', len(set(all_stemmed_text)))
freq_all_docs = find_freq_top50(all_stemmed_text)
print('> frequency top 50 in all documents:', freq_all_docs)
found_25 = find_25percent_freq(all_stemmed_text, freq_all_docs)
print('> how many words to make 25%:', found_25)
