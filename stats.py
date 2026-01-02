def get_word_count(text):
    words = text.split()
    return len(words)

def character_counter(text):
    char_dict = {}
    lower_text = text.lower()

    for character in lower_text:
        char_dict[character] = char_dict.get(character, 0) + 1
    return char_dict
