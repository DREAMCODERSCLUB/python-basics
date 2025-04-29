from collections import Counter

# Step 1: Read the file
with open("sample.txt", "r") as file:   #You need a sample text file to read from
    text = file.read()

# Step 2: Clean and split the text
words = text.lower().split()

# Optional: Remove punctuation
import string
words = [word.strip(string.punctuation) for word in words]

# Step 3: Count total words
print("Total words:", len(words))

# Step 4: Top 5 most frequent words
word_counts = Counter(words)
top_words = word_counts.most_common(5)

print("\nTop 5 words:")
for word, count in top_words:
    print(f"{word}: {count}")