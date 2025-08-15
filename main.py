import sys
from stats import get_num_words, convert_to_lowercase, report

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book = get_book_text(book_path)
    num_words = get_num_words(book)
    lower_words = convert_to_lowercase(book)
    reports = report(lower_words)
    # print(lower_words)
    # print(f"{num_words} words found in the document")
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------\n ")
    for item in reports:
        print(f"{item['char']}: {item['num']}")


main()