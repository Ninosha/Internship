# 2
def word_func(word):
    for i in range(len(word)):
        word = word[::-1]
        k = i
        for j in range(len(word) + 1):
            k += 1
            if k < len(word):
                if word[i] > word[k]:
                    word = list(word)
                    temp = word[i]
                    word[i] = word[k]
                    word[k] = temp
                return "".join(word[::-1])


def final_words_list(words_list):
    listo = []
    for word in words_list:
        if word_func(word) == word:
            listo.append("no result")
        else:
            listo.append(word_func(word))

    return listo
#

words_list = ["ab", "bb", "hefg", "dhck", "dkhc"]
print(final_words_list(words_list))
