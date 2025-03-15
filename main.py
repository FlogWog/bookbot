from stats import word_count

def get_book_text(filepath):
    with open(filepath) as f:
        split_words = f.read()
    return split_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")

main()