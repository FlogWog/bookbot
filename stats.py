def word_count(book_text):
    word_list = book_text.split()
    return len(word_list)

def char_counter(book_text):
    lower_case = book_text.lower()
    char_dict = {}
    for letter in lower_case:
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1

    return char_dict

def sorter(dictionary):
    sorted_list = [] 
    for char, count in dictionary.items():
        sorted_list.append({"character": char, "count": count})

    def sort_on(dict_item):
        return dict_item["count"]

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list