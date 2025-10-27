#
from stats import word_count
from stats import get_book_text
from stats import character_count

def main():
    book = get_book_text("books/frankenstein.txt")
   # print(book)
    num_words = word_count(book)
    #print(f"Found {num_words} total words")
    char_dict = character_count(book)
    print(char_dict)

main()