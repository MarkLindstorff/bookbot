from stats import get_word_count, character_counter

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    ## sti til bog
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    total_words = get_word_count(text)
    chars = character_counter(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in character_counter(text):
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")



if __name__ == "__main__":
    main()