def function0():
    return '0'


def function5(word):
    return word


def function10(word):
    functioned_word = []
    for bit in word:
        if bit == '1':
            functioned_word.append('0')
        else:
            functioned_word.append('1')
    return functioned_word


def function15():
    return '1'
