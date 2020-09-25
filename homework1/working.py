from nltk.corpus import words
import nltk

word_set = set([word.lower() for word in words.words('en')])
min_size_of_word = 2


def append_real_word_combination(all_combinations, characters, visits):
    word = ''.join([characters[i] for i in range(0, len(characters)) if visits[i]])
    if len(word) > min_size_of_word and word in word_set:
        all_combinations.append(word)


def find_all_character_combination(all_combinations, characters, visits, character_index, characters_size, pick_size):
    if pick_size is 0:
        append_real_word_combination(all_combinations, characters, visits)
        return
    if character_index is characters_size:
        return

    visits[character_index] = True
    find_all_character_combination(all_combinations, characters, visits, character_index + 1, characters_size,
                                   pick_size - 1)

    visits[character_index] = False
    find_all_character_combination(all_combinations, characters, visits, character_index + 1, characters_size,
                                   pick_size)


def get_remaining_characters(characters, removed_characters):
    remaining_characters = list(characters)
    for removed_character in removed_characters:
        remaining_characters.remove(removed_character)
    return remaining_characters


def find_all_words(characters):
    if characters is None or len(characters) <= min_size_of_word:
        return False

    all_combinations = list()
    visits = [False for i in range(0, len(characters))]
    for pick_size in range(0, len(characters)):
        if pick_size <= min_size_of_word or pick_size is (len(characters) - 1):
            continue
        find_all_character_combination(all_combinations, characters, visits, 0, len(characters), pick_size)

    for combination in all_combinations:
        combination_characters = list(combination)
        if ''.join(combination_characters) not in word_set:
            continue
        new_characters = get_remaining_characters(characters, combination_characters)
        if new_characters is None or len(new_characters) <= 0:
            return True
        new_word = ''.join(new_characters)
        if new_word in word_set:
            return True
        if find_all_words(new_characters) is True:
            return True
    return False


def contains_found_all(results):
    if results is None:
        return False
    for result in results:
        if result is False:
            return False
    return True


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
    return contains_found_all(result_of_tokens)


if __name__ == '__main__':
    print('Enter the english phrase:')
    user_input = str(input())
    result3 = is_triad(user_input)
    print('Q3. Is triad phrase about "{}": {}'.format(user_input, result3))
