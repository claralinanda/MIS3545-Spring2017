import string
from pprint import pprint

strippables = string.punctuation + string.whitespace

corpus = \
    {'1': 'This class is so cool love it Babson rock',
     '2': 'I learn a lot in BI class I want to be an BI engineer',
     '3': "One of the best class at Babson I love Babson"}

terms = {
    '1': [word.strip(strippables).lower() for word in corpus['1'].split()],
    '2': [word.strip(strippables).lower() for word in corpus['2'].split()],
    '3': [word.strip(strippables).lower() for word in corpus['3'].split()]
}

pprint(terms)
