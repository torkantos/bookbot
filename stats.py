def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def word_count(book_text):
    book = get_book_text("books/frankenstein.txt")
    word_list = book.split()
    num_words = len(word_list)
    return num_words

def character_count(book_text):
    letter_counts = {}
    for letter in book_text:
        lowercase_letter = letter.lower()
        if lowercase_letter in letter_counts:
            letter_counts[lowercase_letter] += 1
        else:
        #elif lowercase_letter not in letter_counts:
            letter_counts[lowercase_letter] = 1
    return letter_counts

