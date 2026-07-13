def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
        
    return count
sentence = input("Enter a string: ") 
result = count_vowels(sentence)
print(f"The number of vowels in the string is: {result}")
