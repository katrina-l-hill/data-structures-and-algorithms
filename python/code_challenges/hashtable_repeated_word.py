from data_structures.hashtable import Hashtable


def first_repeated_word(input):
    # normalize input
    input = input.lower()
    boundary_chars = " \n"
    word_chars = "abcdefghijklmnopqrstuvwxyz'"

    current_word = ""
    word_set = set()

    for char in input:
        if char not in boundary_chars:
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
