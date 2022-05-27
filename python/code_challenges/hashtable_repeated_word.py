from data_structures.hashtable import Hashtable


def first_repeated_word(input):
    word_chars = "abcdefghijklmnopqrstuvxyz"
    word_chars += word_chars.upper()
    word_chars += "'"

    current_word = ""
    word_set = set()

    for char in input:
        if char in word_chars:
            current_word += char
        else:
            if len(current_word) > 0:
                if current_word in word_set:
                    return current_word
                else:
                    word_set.add(current_word)
                    current_word = ""
    if len(current_word) > 0:
        if current_word in word_set:
            return current_word
    return None
