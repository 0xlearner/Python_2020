from collections import Counter

print("Welcome to the Word Frequency Analysis App")

key_phrase = input('Enter a phrase to count the occurrence of words used in a phrase: ').lower().strip()

non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '.', '?', '!', ',', '"', "'", ':', ';', '(', ')',
               '%', '$', '&', '#', '\n', '\t']

for non_letter in non_letters:
    key_phrase = key_phrase.replace(non_letter, ' ')

total_occurrences = len(key_phrase)
word_list = key_phrase.split()
word_count = Counter(word_list)

# Detailed Word Frequency Analysis
print("\nHere is the frequency analysis from phrase: ")
print('\n\tWord\t\tOccurrence\tPercentage')
for key, value in sorted(word_count.items()):
    percentage = round(100 * value / total_occurrences)
    print(f'\n\t{key}\t\t{value}\t\t{percentage}%')

# Orderly most common words in the phrase
ordered_word_count = word_count.most_common()
phrase_ordered_words = []
for pair in ordered_word_count:
    phrase_ordered_words.append(pair[0])
for word in phrase_ordered_words:
    print(f'Most Common words used:{word}')
