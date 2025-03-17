from stats import word_count
from stats import char_counter
from stats import sorter

def get_book_text(filepath):
    with open(filepath) as f:
        split_words = f.read()
    return split_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    char_count = char_counter(book_text)
    sorted_char =  sorter(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")  

    for char_dict in sorted_char:
        char = char_dict["character"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()