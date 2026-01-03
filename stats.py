def get_word_count(text):
    words = text.split()
    return len(words)

def character_counter(text):
    char_dict = {}
    lower_text = text.lower()

    for character in lower_text:
        char_dict[character] = char_dict.get(character, 0) + 1

    sorted_list = [{"char": karakter, "num": værdi} for karakter, værdi in char_dict.items()]
    sorted_list.sort(key=lambda d: d["num"], reverse=True)
    return sorted_list