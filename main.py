import sys

from stats import get_book_text, word_count, character_count, dictionary_list

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        num_words = word_count(book_text)
        char_dictionary = character_count(book_text)
        sorted_dictionary = dictionary_list(char_dictionary)
        
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {book_path}...')
        print('----------- Word Count ----------')
        print(f'Found {num_words} total words')
        print('--------- Character Count -------')
        for item in sorted_dictionary:
            if item['char'].isalpha():
                print (f'{item['char']}: {item['num']}')

        print('============= END ===============')

main()