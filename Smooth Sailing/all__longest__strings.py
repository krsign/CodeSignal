# -*- coding: utf-8 -*-

"""
    Given an array of strings, return another array containing all of its longest strings.
    
    For inputArray = ["aba", "aa", "ad", "vcd", "aba"],
    
    the output should be allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

    @krsign
"""

def allLongestStrings(inputArray):
    
    lenght = map(len, inputArray)
    
    max_len = max(lenght)
    
    return list(filter(lambda x : len(x) == max_len, inputArray))

