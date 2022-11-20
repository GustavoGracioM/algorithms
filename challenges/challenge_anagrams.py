def is_anagram(first_string: str, second_string: str):
    fs = ''
    ss = ''
    if first_string or second_string:
        fs = insertion_sort(first_string.lower())
        ss = insertion_sort(second_string.lower())
        if fs == ss:
            return (fs, ss, True)
    return (fs, ss, False)


def insertion_sort(string):
    list_string = list(string)
    n = len(list_string)

    for index in range(1, n):
        key = list_string[index]

        p = index - 1
        while p >= 0 and list_string[p] > key:
            list_string[p + 1] = list_string[p]
            p = p - 1

        list_string[p + 1] = key

    return "".join(list_string)
