from scipy.spatial import KDTree
import numpy as np

with open('FreqWords.csv', 'r') as file:
    # Create an empty list to store the lines
    lines = []

    # Iterate over the lines of the file
    for line in file:
        line = line.strip()
        lines.append(line.lower())

words = []
vectors = []
for word in lines:
    arr = [0] * 26
    if word =='FreqWords':
        continue
    for letter in word:
        if not letter.isalpha():
            continue
        indx = ord(letter)-ord('a')
        arr[indx] += 1
    words.append(word)
    vectors.append(arr)


vector_array = np.array(vectors)

tree = KDTree(vector_array)

print("Enter query word:")
queryWord = input()
wordArray = [0] * 26
for letter in queryWord:
    if not letter.isalpha():
        continue
    indx = ord(letter)-ord('a')
    wordArray[indx] += 1

distances, indices = tree.query(wordArray, k=10)

result = []
for index in indices:
    result.append(words[index])

print(result)