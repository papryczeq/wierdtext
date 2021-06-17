import random


def shuffle_list(chars):
    """
    Shuffle chars if it's possible.
    """
    # check if there are different letters
    if len(set(chars)) == 1:
        return chars
    result = chars.copy()
    while result == chars:
        random.shuffle(result)
    return result


def match_word(encoded_word, words_list):
    """
    Find first probably correct word
    based on list of words and given encoded word.
    """
    results = []
    for word in words_list:
        #skip all items with different first and last char
        if word[0] != encoded_word[0] or word[-1] != encoded_word[-1]:
            continue
        #skip all items with different chars
        elif sorted(list(word)) != sorted(list(encoded_word)):
            continue
        results.append(word)
    return results[0]