def count_words(text: str) -> int:
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(text: str) -> dict:
    char_counts = {}
    for char in text.lower():
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def sort_dicts(char_counts: dict) -> list:
    sorted = []
    for char in char_counts:
        sorted.append({"char": char,"num": char_counts[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted