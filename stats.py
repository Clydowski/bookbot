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

def sort_characters_by_count(char_dict):
    char_list = [
        {"char": char, "num": count}
        for char, count in char_dict.items()
        if char.isalpha()
    ]
    char_list.sort(key=lambda item: item["num"], reverse=True)
    return char_list

def sort_char_counts(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        sorted_list.append({
            'char': char,
            'count': count
        })

    # Sort the list in place by 'count', descending
    sorted_list.sort(key=lambda d: d['count'], reverse=True)
    return sorted_list