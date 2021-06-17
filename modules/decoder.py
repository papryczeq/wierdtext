import re
from modules.utils import match_word


def decoder(encoded_text):
    """
    Decode string
    """
    try:
        _, text, words = encoded_text.split("\n—weird—\n")
    except ValueError:
        print("Text does not looks like correct output of encoder")

    # fast fix for api - TO REFACTOR
    if 'words' not in locals():
        _, text, words = encoded_text.split("\\n—weird—\\n")

    words = words.split(" ")
    result = list(text)
    for m in re.finditer(r'\b[A-Za-z]{4,}\b', text):
        start = m.start()
        end = m.end()
        word = match_word(m.group(), words)
        result[start:end] = list(word)
        words.remove(word)
    return "".join(result)