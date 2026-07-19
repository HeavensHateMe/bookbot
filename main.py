import sys
from stats import word_count_in_text, chars_dict_to_sorted_list
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def print_report(path_to_file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_in_text(path_to_file)} total words")
    print("--------- Character Count -------")
    alphabetical_sorted_list = []
    for tuple in chars_dict_to_sorted_list(path_to_file):
        if tuple[0].isalpha():
            alphabetical_sorted_list.append(tuple)
        else:
            continue
    for char_int in alphabetical_sorted_list:
        print(f"{char_int[0]}: {char_int[1]}")
    print("============= END ===============")
    return None

def main():
    print_report(sys.argv[1])
main()
