def word_analyzer():
    text = input("Enter a paragraph: ")

    words = text.split()
    word_count = len(words)

    # Find longest word
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    # Count vowels
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1

    
    print("\n--- Word Analyzer ---")
    print("Total Words:", word_count)
    print("Longest Word:", longest_word)
    print("Total Vowels:", vowel_count)

word_analyzer()
