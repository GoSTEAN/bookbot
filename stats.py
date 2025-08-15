
def get_num_words(word):
    words = word.split()
    return len(words)


def convert_to_lowercase(word):
    counts = {}
    for char in word.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_on(d):
    return d["num"]

def report(dict_word):
    sort_dic = []

    for char, count in dict_word.items():
        if char.isalpha():
            sort_dic.append({"char": char, "num": count})

    sort_dic.sort(key=sort_on, reverse=True,)
    return sort_dic