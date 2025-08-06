def get_num_words(filepath):
    words = filepath.split()
    return len(words)

def get_char_counts(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts
