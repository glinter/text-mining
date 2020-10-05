# XML Parsing Example01
# import xml.etree.ElementTree as et
#
# tree = et.ElementTree(file='menu.xml')
# root = tree.getroot()
# print(root)
# # > <Element 'menu' at 0x0000011625623548>
#
# for child in root:
#     print('tag:', child.tag, ', attribute:', child.attrib)
#     for grandchild in child:
#         print('\ttag:', grandchild.tag, ', attribute:', grandchild.attrib)
# # > tag: breakfast , attribute: {'hours': '7-11'}
# # > 	tag: item , attribute: {'price': '$6.00'}
# # > 	tag: item , attribute: {'price': '$4.00'}
# # > tag: lunch , attribute: {'hours': '11-3'}
# # > 	tag: item , attribute: {'price': '$5.00'}
# # > tag: dinner , attribute: {'hours': '3-10'}
# # > 	tag: item , attribute: {'price': '8.00'}
#
# print('children count of root:', len(root))
# # > children count of root: 3
# print('children count of first child:', len(root[0]))
# # > children count of first child: 2
#
# print('first child:', root[0])
# # > first child: <Element 'breakfast' at 0x00000250C21335E8>
# print('attribute hours from first child:', root[0].get('hours'))
# # > attribute hours from first child: 7-11
# print('attribute keys from first child:', root[0].keys())
# # > attribute keys from first child: ['hours']
# print('attribute key-value items from first child:', root[0].items())
# # > attribute key-value items from first child: [('hours', '7-11')]
#
# lunch = root.find('lunch')
# print('lunch child:', lunch)
# # > lunch child: <Element 'breakfast' at 0x00000250C21335E8>
# print('attribute hours from lunch child:', lunch.get('hours'))
# # > attribute hours from lunch child: 7-11
# print('attribute keys from lunch child:', lunch.keys())
# # > attribute keys from lunch child: ['hours']
# print('attribute key-value items from lunch child:', lunch.items())
# # > attribute key-value items from lunch child: [('hours', '7-11')]
#
# print()
# print(root[0].find('item').items())
# print(root[0].findall('item'))

# Json Example01
# import json
# j1 = {'name': '홍길동', 'birth': '0525', 'age': 30}
# print(type(j1))
# print(type(json.dumps(j1)))
# print(json.dumps(j1, indent=2))
# dump_data = json.dumps(j1, indent=2)
# print(type(json.loads(dump_data)))

# urllib Example01
# from urllib.request import urlopen
#
# html = urlopen('http://pythonscraping.com/pages/page1.html')
# print(type(html.read()))

# BeautifulSoup Example01
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen('http://pythonscraping.com/pages/page1.html')
# bs_obj = BeautifulSoup(html.read(), 'html.parser')
# print(bs_obj.h1)

# Scraping Example01
import nltk, re, pprint
from nltk import word_tokenize
from urllib import request

url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
response = request.urlopen(url)
raw = response.read().decode('utf-8')
print(type(raw))
print(len(raw))
print(raw[:100])
tokens = word_tokenize(raw)
print(tokens[:10])
text = nltk.Text(tokens)
print(type(text))
print(text[1024:1062])
print(raw.find('PART 1'))
print(raw.rfind('End of Project Gutenberg'))
raw = raw[5336:1157810]
print(raw[-100:])

