def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text_string):
    text_string = text_string.lower()
    characters = set()
    character_dictionary = {}
    for char in text_string:
        if char not in characters:
            characters.add(char)
            character_dictionary[char] = 1
        else:
            character_dictionary[char] = character_dictionary[char] + 1
    return character_dictionary


def sort_on(items):
    return items['num']


def dictionary_list(list_to_sort):
    new_list = []
    for item in list_to_sort:
        new_list.append({'char': item, 'num': list_to_sort[item]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list





#test = {'a': 10, 'd': 20, 'e': 1}
#result = dictionary_list(test)
#print(result)

#result.sort(reverse=True, key=sort_on)
#print(result)

#est.sort(key=dictionary_sort, reverse=False)
#rint(test)
#test = "abcdefgh ijkl;mnaop:qrst,uv.w"

#result = character_count(test)
#print(result)
