from WordSearchKDTree import WordSearchKDTree
from WordSearchRTree import WordSearchRTree
from sklearn.decomposition import PCA

TOTAL_NEIGHBORS = 10
PCA_DIMENSION = 15

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

ktree = WordSearchKDTree(words, vectors)
rtree = WordSearchRTree(words, vectors)

print("Enter query word:")
queryWord = input()
wordArray = [0] * 26
for letter in queryWord:
    if letter not in "qazxswedcvfrtgbnhyujmikolp":
        continue
    indx = ord(letter)-ord('a')
    wordArray[indx] += 1

ktree.query(wordArray, TOTAL_NEIGHBORS)

rtree.query(wordArray, TOTAL_NEIGHBORS)

pca = PCA(n_components=PCA_DIMENSION)  

reduced_vectors = pca.fit_transform(vectors)
reducedktree = WordSearchKDTree(words, reduced_vectors)
reducedrtree = WordSearchRTree(words, reduced_vectors)
print("Reduce Dimension")
reducedWordArray = pca.transform([wordArray])[0]

reducedktree.query(reducedWordArray, TOTAL_NEIGHBORS)
reducedrtree.query(reducedWordArray, TOTAL_NEIGHBORS)