import sys
from stats import get_word_count, get_char_count, get_sort_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        words_counted = get_word_count(book_text)
        characters_counted = get_char_count(book_text)
        sorted_list = get_sort_list(characters_counted)
        print_report(book_path, words_counted, sorted_list)

def print_report(path, count_word, list_sort):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {count_word} total words')
    print('--------- Character Count -------')
    for d in list_sort:
        if not d["char"].isalpha():
            continue
        print(f"{d["char"]}: {d["num"]}")
    print('============= END ===============')

main()