def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
        return file_contents

def word_count_in_text(path_to_file):
    text = get_book_text(path_to_file)
    text_list = text.split()
    word_count = len(text_list)
    return word_count

def character_count_in_text(path_to_file):
    text = get_book_text(path_to_file)
    character_count_dict = {}
    for character in text:
        char = character.lower()
        if char not in character_count_dict:
            character_count_dict[char] = 1
        else:
            character_count_dict[char] += 1
    return character_count_dict

def sort_on(tuple):
    return tuple[1]

def chars_dict_to_sorted_list(path_to_file):
    sorted_list = []
    character_count_dict = character_count_in_text(path_to_file)
    for key_char in character_count_dict:
        tuple = (key_char,character_count_dict[key_char])
        sorted_list.append(tuple)
    sorted_list = sorted(sorted_list, reverse=True, key=sort_on)
    return sorted_list
