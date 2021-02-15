from typing import Iterable


def median_three(els: Iterable[int]) -> Iterable[int]:
    """

    :type els: object
    """
    # your code here
    a = []
    b = []
    temp_elem = []
    a = els[:2]
    print(els, 'ELS')
    for i in range(len(els)):
        if  i + 2 < len(els):
            temp_elem = els[i:i + 3]
            v = sorted(temp_elem)
            print(temp_elem, 'SORTED')
            b = v[1]
            a.append(b)
    print(a, 'READy')
    return a


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([5,2,9,1,7,4,6,3,8])) == [5,2,5,2,7,4,6,4,6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
