from typing import Iterable


def median_three(els: Iterable[int]) -> Iterable[int]:
    # your code here
    a = []
    b = []
    temp_elem = []
    a = els[:2]
    print(els,'ELS')
    for i in range(len(els)):
        if not i+2 == len(els):
            temp_elem = els[i:i+3]
            sorted(temp_elem)
            print(temp_elem, 'SORTED')


    print(a, 'READy')
    return a



if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
