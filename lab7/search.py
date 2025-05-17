from matrix import get_word


def g_l_search(binary_matrix, arg):
    words = []
    g_start = False
    l_start = False
    g_values = []
    l_values = []
    for word_number in range(16):
        word = get_word(binary_matrix, word_number)
        words.append(word)
    for word in words:
        for i in range(16):
            g = g_start or (not bool(int(arg[i])) and bool(int(word[i])) and not l_start)
            l = l_start or (bool(int(arg[i])) and not bool(int(word[i])) and not g_start)
            g_start = g
            l_start = l
        g_values.append(g_start)
        l_values.append(l_start)
    counts = []
    count = 0
    for word in words:
        for i in range(16):
            if word[i] == arg[i]:
                count += 1
        counts.append(count)
        count = 0
    return g_values, l_values, counts, words


