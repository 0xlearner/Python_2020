from itertools import permutations
from typing import List

print('Welcome to the Name Mashup Game')

names = [
    input('Enter one full name(FIRST LAST): ').split(),
    input('Enter second full name(FIRST LAST): ').split(),
    # input('Enter third full name(FIRST LAST):' ).split(),  <- try me!
]

def mash(first: List[str], second: List[str]) -> List[str]:
    """
    Produce a list where each element has the first half of the corresponding
    element from the first list and the second half of the corresponding
    element from the second list.

    For example:
        mash(['AA', 'BB'], ['XX', 'YY']) -> ['AX', 'BY']
    """
    return [
        a[:len(a)//2] + b[len(b)//2:]
        for a, b in zip(first, second)
    ]

for first, second in permutations(names, 2):
    print(' '.join(mash(first, second)))