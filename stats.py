def get_word_count(file_path):
    with open(file_path) as file:
        text = file.read()

    words = text.split()
    return len(words)