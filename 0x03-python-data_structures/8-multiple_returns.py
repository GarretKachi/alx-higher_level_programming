#!/usr/bin/python3
# Return len of str and its first character


def multiple_returns(sentence):

    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
