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

def sort_on(items):
    return items["num"]

def report(dict):
    book = get_book_text("books/frankenstein.txt")
    letter_dict = character_count(book)
    dict_list = []]
    for item in letter_dict.items():
        if item.isalpha():
            dict_list.append({"char":item, "num": count})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    
