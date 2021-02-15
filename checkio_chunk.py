from typing import Iterable


def chunking_by(items: list, size: int) -> Iterable:
    # your code here
    temp_item = []
    new_item = []
    if items == new_item:
        a = 1
        return items
    for i in items:
        if len(temp_item) < size:
            temp_item.append(i)
        else:
            new_item.append(temp_item)
            temp_item = []
            temp_item.append(i)
    new_item.append(temp_item)
    print(new_item)
    return new_item


if __name__ == '__main__':
    print("Example:")
    print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
    assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
    assert list(chunking_by([5, 4], 7)) == [[5, 4]]
    assert list(chunking_by([], 3)) == []
    assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]
    print("Coding complete? Click 'Check' to earn cool rewards!")
