# from nltk.corpus import words


# 1. 단어를 입력했을 때 그 단어의 철자가 맞는 지를 체크하는 함수를 작성하고 실행해보라. (단수만 체크)
# (힌트) 영어 단어 리스트는 nltk 패키지의 words를 import 해서 사용
# (nltk 패키지는 강의교안 참고)
# (힌트) if 문으로 체크할 때 in 연산자를 활용하라
# (힌트) 함수의 매개변수로 체크할 단어 w 와 앞에서 생성한 단어 리스트 words를 사용하라
# def check_english_word_spell(w):
#     target_word = w.strip().lower()
#     word_list = [word.lower() for word in words.words('en')]
#     return target_word in word_list
#
#
# if __name__ == '__main__':
#     print('Enter the english word:')
#     user_input = str(input())
#     result1 = check_english_word_spell(user_input)
#     print('Q1. Check spell about "{}": {}'.format(user_input, result1))


# 2. dictionary 구조의 자료를 하나 생성하고 key와 value를 바꾸어서 딕셔너리에 저장하는 함수(flip)를 구현하라.
# 그 함수를 불러서 실행하라. 다음과 똑같은 예를 사용하지 않아도 되지만,
# 원래 데이터에서 value가 같은 게 있을 때의 처리를 위해 신규 dictionary는 value를 list로 저장하라.
# >flip({"잡채": "한식", "갈비탕": "한식", "초밥": "일식", ＂짜장면": "중식"})
# {"한식": ["잡채", "갈비탕”], "일식”: ["초밥”]:, "중식": ["짜장면 "]}
# def flip(target_dict):
#     result = {item[1]: list() for item in target_dict.items()}
#     for item in target_dict.items():
#         key = item[1]
#         value = item[0]
#         result[key].append(value)
#     return result
#
#
# if __name__ == '__main__':
#     my_dict = dict()
#     my_dict['잡채'] = '한식'
#     my_dict['갈비탕'] = '한식'
#     my_dict['초밥'] = '일식'
#     my_dict['짜장면'] = '중식'
#     result2 = flip(my_dict)
#     print('Q2. Flip dictionary "{}": \n=> {}'.format(my_dict, result2))


# # 3. 입력되는 문장이 triad phrases 인지를 판별하는 함수를 구현하고 이 함수를 불러서 실행하라.
# # is_triad("learned theorem") => True
# # is_triad("studied theories") => False
# # is_triad("wooded courses") => True
from nltk.corpus import words
import nltk

word_set = set([word.lower() for word in words.words('en')])


def find_word(base_word_index, characters, find_word_length, current_word):
    if find_word_length >= len(characters):
        if find_word_length == len(current_word) and current_word in word_set:
            return current_word
        else:
            return None
    if find_word_length == len(current_word) and current_word in word_set:
        return current_word

    current_word = characters[base_word_index]
    for i in range(0, len(characters)):
        if i is base_word_index:
            continue
        if len(current_word) == find_word_length:
            if current_word in word_set:
                return current_word
            else:
                current_word = characters[base_word_index]
        current_word = current_word + characters[i]
    return find_word(base_word_index, characters, find_word_length + 1, characters[base_word_index])

def remove_word_2_list(word, my_list):
    for character in list(word):
        my_list.remove(character)
    return my_list

def find_all_words(remaining_characters):
    if len(remaining_characters) <= 0:
        return True
    print('find_all_words:', remaining_characters)
    characters = remaining_characters
    for i in range(0, len(characters)):
        base_word = characters[i]
        found_word = find_word(i, characters, 3, base_word)
        if found_word is not None:
            print(found_word)
            new_remaining_characters = remove_word_2_list(found_word, remaining_characters)
            return find_all_words(new_remaining_characters)
    return False


def is_triad(phrase):
    def contains_found_all(results):
        if results is None:
            return False
        for result in results:
            if result is False:
                return False
        return True

    lowercase_phrase = phrase.lower()
    tokens = nltk.word_tokenize(lowercase_phrase)
    result_of_tokens = [False for i in range(len(tokens))]
    for t in range(len(tokens)):
        token = tokens[t]
        characters = list(token)
        found = find_all_words(characters)
        if found is True:
            result_of_tokens[t] = True
    return contains_found_all(result_of_tokens)


if __name__ == '__main__':
    print('Enter the english phrase:')
    # user_input = str(input())
    user_input = 'learned'
    result3 = is_triad(user_input)
    print('Q3. Is triad phrase about "{}": {}'.format(user_input, result3))
