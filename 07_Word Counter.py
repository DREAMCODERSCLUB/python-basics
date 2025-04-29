# Word Counter

print("Word Counter")

text = input("Enter a sentence or paragraph:\n")
words = text.split()

word_count = {}

for word in words:
    word = word.lower().strip('.,!?')  # Clean punctuation
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")
