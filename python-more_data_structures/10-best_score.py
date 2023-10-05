#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        big_key = sorted(a_dictionary, key=a_dictionary.get, reverse=True)
        return big_key[0]
    else:
        return None
