def word_count(text):
    if text.strip() == "":
        return 0
    return len(text.split())
def unique_word(text):
    words = text.split()
    unique = []

    for word in words:
        if word not in unique:
            unique.append(word)
    return unique

def reverse_string(text):
    return text[::-1]