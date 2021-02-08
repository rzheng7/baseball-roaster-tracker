from typing import DefaultDict


def find_char_count(s):
    """[summary]

    Args:
        s ([type]): [description]

    Returns:
        [type]: [description]
    """

    if len(s) == 0:
        return []

    pre = s[0]
    char_count = list()
    count = 0

    for cur in s:
        if pre == cur:
            count += 1

        if pre != cur:
            char_count.append((pre, count))  
            pre = cur
            count = 1
    char_count.append((cur, count))
    
    return char_count


# dd = DefaultDict(list)
# dd['a'].append(10)
# dd['b'].extend(find_char_count("aaaabbccca"))
# dd['b'].append(10)
# print(dd)

assert find_char_count("aaaabbccca") == [('a', 4),
                                         ('b', 2),
                                         ('c', 3),
                                         ('a', 1)]
assert find_char_count("a") == [('a', 1)]
assert find_char_count("aa") == [('a', 2)]
assert find_char_count("") == []
