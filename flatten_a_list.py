def flat_list(array):

    a = True
    temp_array = []
    flag_list = 0
    while a:
        for i in array:
            if isinstance(i, list):
                temp_array.extend(i)
                print('proverka')
                flag_list = 1
            else:
                temp_array.append(i)
        print(temp_array)
        if flag_list == 1:
            a = True
            array = temp_array
            temp_array = []
        else:
            a = False
        flag_list = 0
    return array

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')