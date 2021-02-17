import time

def flat_list(array):
    a = True
    temp_array = []
    flag_list = 0
    while a:
        for i in array:
            if isinstance(i, list):
                temp_array.extend(i)
                flag_list = 1
            else:
                temp_array.append(i)
        if flag_list == 1:
            a = True
            array = temp_array
            temp_array = []
        else:
            a = False
        flag_list = 0
    return array

def rec_func(array):
    new_array = []
    for i in array:
        if isinstance(i, list):
            new_array.extend(rec_func(i))
        else:
            new_array.append(i)
    print(new_array)
    return new_array




if __name__ == '__main__':
    start_time = time.time()
    assert rec_func([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    print("--- %s seconds ---" % (time.time() - start_time))
    print('Done! Check it')