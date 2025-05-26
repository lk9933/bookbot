import sys
from stats import count_words, count_characters, sort_dicts

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    print(f"Analyzing book found at {file_path}...")
    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_counts = count_characters(text)
    sorted_counts = sort_dicts(char_counts)
    for char_dict in sorted_counts:
        char = char_dict["char"]
        if not str.isalpha(char):
            pass
        else:
            count = char_dict["num"]
            print(f"{char}: {count}")
    print("============= END ===============")

main()