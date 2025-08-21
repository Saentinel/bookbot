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
    character_dictonary = {}
    for char in text_string:
        if char not in characters:
            characters.add(char)
            character_dictonary[char] = 1
        else:
            character_dictonary[char] = character_dictonary[char] + 1
    return character_dictonary

#test = "abcdefgh ijkl;mnaop:qrst,uv.w"

#result = character_count(test)
#print(result)
