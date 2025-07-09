# word_counter.py

def count_words(sentence):
    # Convert to lowercase and remove punctuation for better counting
    sentence = sentence.lower()
    # Simple punctuation removal (you can expand this)
    for char in ",.!?;:":
        sentence = sentence.replace(char, "")

    words = sentence.split() # Split the sentence into words
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        
    return word_counts

def main():
    text = input("Enter a sentence or paragraph: ")
    counts = count_words(text)
    print("\nWord Counts:")
    for word, count in sorted(counts.items()): # Sort for consistent output
        print(f"'{word}': {count}")

if __name__ == "__main__":
    main()