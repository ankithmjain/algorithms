#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    note_dict = {}
    for value in note:
        if value not in magazine:
            print(value)
            return "No"
        if note_dict.get(value) is None:
            note_dict[value] = 1
        else:
            print(note_dict[value], value)
            return "No"
    return "Yes"

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
