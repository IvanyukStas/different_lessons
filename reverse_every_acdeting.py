def reverse_ascending(items):
    # your code here
    temp_items = []
    new_items = []
    for i in range(len(items)):
        if i == len(items)-1:
            temp_items.append(items[i])
            temp_items.reverse()
            for j in temp_items:
                new_items.append(j)
            continue
        if items[i] < items[i+1]:
            temp_items.append(items[i])
        else:
            temp_items.append(items[i])
            temp_items.reverse()
            new_items.extend(temp_items)
            temp_items = []
    print(temp_items)
    print(new_items)
    return new_items


if __name__ == '__main__':
    print("Example:")

    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
