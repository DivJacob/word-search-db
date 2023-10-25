from scipy.spatial import KDTree
import numpy as np
import sys

sys.setrecursionlimit(10000)

with open("allwords_dataset.csv", 'r') as file:
    # Create an empty list to store the lines
    lines = []

    # Iterate over the lines of the file
    for line in file:
        
        line = line.strip()
        line=line.lower()
        line=line.split(',')
        lines.append(line[1].lower())


words = []
vectors = []
for word in lines:
    arr = [0] * 26
    for letter in word:
        if letter not in "qazxswedcvfrtgbnhyujmikolp":
            continue
        indx = ord(letter)-ord('a')
        arr[indx] += 1
    words.append(word)
    vectors.append(arr)

vector_array = np.array(vectors)

print(vector_array.shape)

tree = KDTree(vector_array)

print("Enter query word:")
queryWord = input()
wordArray = [0] * 26
for letter in queryWord:
    if letter not in "qazxswedcvfrtgbnhyujmikolp":
        continue
    indx = ord(letter)-ord('a')
    wordArray[indx] += 1

distances, indices = tree.query(wordArray, k=10)

result = []
for index in indices:
    result.append(words[index])

print(result)



    