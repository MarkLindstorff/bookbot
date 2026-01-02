"""
lavet til første opgave, return hele teksten fra filen.

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
"""


"""
get_word_count, tager filen og åbner den, 
derefter splitter den teksten og tæller hvor mange ord der er.
"""
def get_word_count(file_path):
    with open(file_path) as file:
        text = file.read()

    words = text.split()
    return len(words)

    
def main():
    ## sti til bog
    book_path = "books/frankenstein.txt"

    ## ord tæller call
    total_words = get_word_count(book_path)
    print(f"Found {total_words} total words")



if __name__ == "__main__":
    main()