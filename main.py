from stats import get_num_words, get_char_counts, sort_char_counts
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...\n")

    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words\n")

    print("--------- Character Count -------")
    char_counts = get_char_counts(text)
    sorted_char_counts = sort_char_counts(char_counts)

    for entry in sorted_char_counts:
        print(f"{entry['char']}: {entry['count']}")
    
    print("\n============= END ===============")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()