def count_word_frequency(words):
  word_counts = {}
  #  Place keys with initial value of 0
  for word in words:
    word_counts[word] = 0
  # add 1 for every instance of the word
  for word in words:
    word_counts[word] += 1

  return word_counts

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words))


""" 
def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
 """