def flatten(dictionary):
    # your code here
    flatten_dict = {}
    for k, v in dictionary.items():
        if v == {}:
            v = ""
            flatten_dict[k] = v
        if isinstance(v, dict):
            flatten_dict.update(flatten(v))
            for c, y in flatten_dict.items():
                flatten_dict[k+'/'+c] = flatten_dict.pop(c)
                break
        else:
            if v == {}:
                v = ""
            flatten_dict[k] = v
    print(flatten_dict)
    return flatten_dict
if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
