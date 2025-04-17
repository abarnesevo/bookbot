from stats import word_count, character_count
import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        print(f"Analyzing book found at {sys.argv[1]}")
        file_contents = f.read()
    return file_contents    


def main():
    if len(sys.argv) != 2:
        print("bookbot needs two command line arguments to function")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        print("============ BOOKBOT ============")
        file_contents = get_book_text()
        counted_words = word_count(file_contents)
        counted_characters = character_count(file_contents)
        print("----------- Word Count ----------")
        print(f"Found {counted_words} total words")
        print("--------- Character Count -------")
        for char in counted_characters:
            print(f"{char["char"]}: {char["count"]}")
        print("============= END ===============")
main()
