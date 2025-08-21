from stats import get_book_text
from stats import word_count
from stats import character_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    char_dictonary = character_count(book_text)
    print(f'{num_words} words found in the document')
    print(char_dictonary)

main()