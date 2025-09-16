def get_word_count(text):
    count_word = text.split()
    return len(count_word)

def get_char_count(string_text):
    characters = string_text.lower()
    count_char = {}
    for char in characters:
        if char not in count_char:
            count_char[char] = 1
        else:
            count_char[char] += 1
    return count_char

def sort_on(item):
    return item["num"]

def get_sort_list(list):
    sort_list = []
    for i in list:
        sort_list.append({"char": i, "num": list[i]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list