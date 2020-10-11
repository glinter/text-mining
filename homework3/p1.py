import re
from enum import Enum, auto


class RegexType(Enum):
    MATCH = auto()
    SKIP = auto()


def refine_regex(regex):
    chars = [char for char in regex]
    new_chars = []
    for char in chars:
        revised_char = char
        if char in ['.', '+', '*', '$', '?']:
            revised_char = '\\' + char
        new_chars.append(revised_char)
    return ''.join(new_chars)


def inspect_skip(regex, text):
    pattern = re.compile('^(?!(' + regex + '))\\w+')
    return pattern.search(text)


def inspect_match(regex, text):
    pattern = re.compile(regex)
    return pattern.search(text)


def print_inspect(regex_type, regex_string, text):
    revised_regex = refine_regex(regex_string)
    result = None
    if regex_type is RegexType.MATCH.name:
        result = inspect_match(revised_regex, text)
    elif regex_type is RegexType.SKIP.name:
        result = inspect_skip(revised_regex, text)
    else:
        raise Exception('Can not find regex_type')
    print('[{}]{} - {}\n\t {}'.format(regex_type, regex_string, text, str(result)))


def print_3_texts(regex_type, regex_string):
    print_inspect(regex_type, regex_string, regex_string)
    print_inspect(regex_type, regex_string, 'Hello&!+=' + regex_string + '&132')
    print_inspect(regex_type, regex_string, 'Hello')


# Question1
print('> Question 1')
print_3_texts(RegexType.MATCH.name, 'abc123xyz')
print_3_texts(RegexType.MATCH.name, 'define "123"')
print_3_texts(RegexType.MATCH.name, 'var g = 123;')

# Question2
print('\n> Question 2')
print_3_texts(RegexType.MATCH.name, 'cat.')
print_3_texts(RegexType.MATCH.name, '896.')
print_3_texts(RegexType.SKIP.name, 'abc1')

print('\n> Question 3')
print_3_texts(RegexType.MATCH.name, 'can')
print_3_texts(RegexType.MATCH.name, 'man')
print_3_texts(RegexType.MATCH.name, 'fan')
print_3_texts(RegexType.SKIP.name, 'dan')
print_3_texts(RegexType.SKIP.name, 'ran')
print_3_texts(RegexType.SKIP.name, 'pan')

print('\n> Question 4')
print_3_texts(RegexType.MATCH.name, 'hog')
print_3_texts(RegexType.MATCH.name, 'dog')
print_3_texts(RegexType.SKIP.name, 'bog')

print('\n> Question 5')
print_3_texts(RegexType.MATCH.name, 'Ana')
print_3_texts(RegexType.MATCH.name, 'Bob')
print_3_texts(RegexType.MATCH.name, 'Cpc')
print_3_texts(RegexType.SKIP.name, 'aax')
print_3_texts(RegexType.SKIP.name, 'bby')
print_3_texts(RegexType.SKIP.name, 'ccz')

print('\n> Question 6')
print_3_texts(RegexType.MATCH.name, 'wazzzzzup')
print_3_texts(RegexType.MATCH.name, 'wazzzup')
print_3_texts(RegexType.SKIP.name, 'wazup')

print('\n> Question 7')
print_3_texts(RegexType.MATCH.name, 'aaaabcc')
print_3_texts(RegexType.MATCH.name, 'aabbbbc')
print_3_texts(RegexType.MATCH.name, 'aacc')
print_3_texts(RegexType.SKIP.name, 'a')

print('\n> Question 8')
print_3_texts(RegexType.MATCH.name, '1 file found?')
print_3_texts(RegexType.MATCH.name, '2 file found?')
print_3_texts(RegexType.MATCH.name, '24 files found?')
print_3_texts(RegexType.SKIP.name, 'No files found.')

print('\n> Question 9')
print_3_texts(RegexType.MATCH.name, '1. abc')
print_3_texts(RegexType.MATCH.name, '2.     abc')
print_3_texts(RegexType.MATCH.name, '3.         abc')
print_3_texts(RegexType.SKIP.name, '4.abc')
