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
min_size_of_word = 2


def append_real_word_combination(all_combinations, characters, visits):
    word = ''.join([characters[i] for i in range(0, len(characters)) if visits[i]])
    if len(word) > min_size_of_word and word in word_set:
        all_combinations.append(word)


def find_all_character_combination(all_combinations, characters, visits, character_index, pick_size):
    if pick_size is 0:
        append_real_word_combination(all_combinations, characters, visits)
        return
    if character_index is len(characters):
        return

    visits[character_index] = True
    find_all_character_combination(all_combinations, characters, visits, character_index + 1, pick_size - 1)

    visits[character_index] = False
    find_all_character_combination(all_combinations, characters, visits, character_index + 1, pick_size)


def get_remaining_characters(characters, removed_characters):
    remaining_characters = list(characters)
    for removed_character in removed_characters:
        remaining_characters.remove(removed_character)
    return remaining_characters


def find_all_words(characters):
    if len(characters) <= min_size_of_word:
        return False

    all_combinations = list()
    visits = [False for i in range(0, len(characters))]
    for pick_size in range(0, len(characters)):
        if pick_size <= min_size_of_word or pick_size is (len(characters) - 1):
            continue
        find_all_character_combination(all_combinations, characters, visits, 0, pick_size)

    for combination in all_combinations:
        combination_characters = list(combination)
        if ''.join(combination_characters) not in word_set:
            continue
        remaining_characters = get_remaining_characters(characters, combination_characters)
        if remaining_characters is None or len(remaining_characters) <= 0:
            print(''.join(characters), '=', ''.join(combination_characters), '/', ''.join(remaining_word))
            return True
        remaining_word = ''.join(remaining_characters)
        if remaining_word in word_set:
            print(''.join(characters), '=', ''.join(combination_characters), '//', ''.join(remaining_word))
            return True
        if find_all_words(remaining_characters) is True:
            print(''.join(characters), '=', ''.join(combination_characters), '///', ''.join(remaining_word))
            return True
    return False


def is_triad(phrase):
    lowercase_phrase = phrase.lower()
    tokens = nltk.word_tokenize(lowercase_phrase)
    result_of_tokens = [False for i in range(len(tokens))]
    for t in range(len(tokens)):
        token = tokens[t]
        characters = list(token)
        found = find_all_words(characters)
        if found is True:
            result_of_tokens[t] = True
    return not(False in result_of_tokens)


if __name__ == '__main__':
    print('Enter the english phrase:')
    user_input = str(input())
    result3 = is_triad(user_input)
    print('Q3. Is triad phrase about "{}": {}'.format(user_input, result3))
