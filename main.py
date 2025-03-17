from stats import word_count
from stats import char_counter
from stats import sorter
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        split_words = f.read()
    return split_words

def main(filepath):
    book_text = get_book_text(filepath)
    num_words = word_count(book_text)
    char_count = char_counter(book_text)
    sorted_char =  sorter(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")  

    for char_dict in sorted_char:
        char = char_dict["character"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    main(filepath)