def find_longest_word():
    words = input("Enter a list of words separated by spaces: ").split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

longest = find_longest_word()
print(f"The longest word is: {longest}")
