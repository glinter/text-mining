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
        if char in ['.', '+', '*', '$']:
            revised_char = '\\' + char
        new_chars.append(revised_char)
    return ''.join(new_chars)


def inspect_skip(regex, text):
    pattern = re.compile('^((?!' + regex + '))*$')
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


# Question1
print('> Question 1')
print_inspect(RegexType.MATCH.name, 'abc123xyz', 'abc123xyz')
print_inspect(RegexType.MATCH.name, 'abc123xyz', 'Hello&!+=abc123xyz')
print_inspect(RegexType.MATCH.name, 'define "123"', 'define "123"')
print_inspect(RegexType.MATCH.name, 'define "123"', 'Hello&!+=define "123"fgdfgdfgfdg')
print_inspect(RegexType.MATCH.name, 'var g = 123;', 'var g = 123;')
print_inspect(RegexType.MATCH.name, 'var g = 123;', 'Hello&!+=var g = 123;dfgdfgdfgdfg')

# Question2
print('\n> Question 2')
print_inspect(RegexType.MATCH.name, 'cat.', 'cat.')
print_inspect(RegexType.MATCH.name, 'cat.', 'Hello&!+=cat.asdfadf')
print_inspect(RegexType.MATCH.name, '896.', '896.')
print_inspect(RegexType.MATCH.name, '896.', 'Hello&!+=896.')
print_inspect(RegexType.SKIP.name, 'abc1', 'abc1')
print_inspect(RegexType.SKIP.name, 'abc1', 'Hello&!+=abc1#ersdfsdfdsf')
print_inspect(RegexType.SKIP.name, 'abc1', 'Hello')

