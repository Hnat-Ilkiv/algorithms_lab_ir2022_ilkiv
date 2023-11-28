def knuth_morris_pratt(haystack, needle):
    if not needle:
        return []

    prefix_function = [0] * len(needle)
    j = 0
    for i in range(1, len(needle)):
        while j > 0 and needle[i] != needle[j]:
            j = prefix_function[j - 1]
        if needle[i] == needle[j]:
            j += 1
        prefix_function[i] = j

    indices = []
    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = prefix_function[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            indices.append(i - j + 1)
            j = prefix_function[j - 1]

    return indices
