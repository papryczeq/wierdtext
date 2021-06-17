import re
import random
from modules.utils import shuffle_list


def encoder(text):
    """
    Encode given string.
    """
    result = list(text)
    words_list = []
    for m in re.finditer(r'\b[A-Za-z]{4,}\b', text):    #return word and its indexes on the list
        words_list.append(m.group())
        start = m.start() + 1
        end = m.end() - 1
        result[start:end] = shuffle_list(result[start:end])
    result = "".join(result)
    words_list = sorted(words_list, key=str.lower)
    magic_value = "\n—weird—\n"
    
    return magic_value + result + magic_value + " ".join(words_list)