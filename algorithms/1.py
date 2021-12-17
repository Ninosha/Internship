# 1


def word_counter(words_list, n):
    count_dict = {}
    for word in words_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return f'''{len(count_dict)}\n{" ".join([str(num) for num in count_dict.values()])}'''


words_list = []

number = int(input())
for i in range(number):
    word = input()
    words_list.append(word)

print(word_counter(words_list,number))
