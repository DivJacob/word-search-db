from WordSearchKDTree import WordSearchKDTree
from WordSearchRTree import WordSearchRTree
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

TOTAL_NEIGHBORS = 10
PCA_DIMENSION = 15
VECTOR_TYPE = 1
ENABLE_PCA = False
ENABLE_RTREE = False

def generate_vector(word, type):
    arr = [0] * 26
    if type == 1: # Word Frequency Vector
        for letter in word:
            if letter not in "qazxswedcvfrtgbnhyujmikolp":
                continue
            indx = ord(letter)-ord('a')
            arr[indx] += 1
    else: # Ascii Vector
        indx = 0
        for letter in word:
            if letter not in "qazxswedcvfrtgbnhyujmikolp":
                continue
            arr[indx] = ord(letter)-ord('a')
            indx += 1
            if indx == 26:
                break
    return arr
    
with open("words_alpha.txt", 'r') as file:
    # Create an empty list to store the lines
    lines = []

    # Iterate over the lines of the file
    for line in file:
        
        line = line.strip()
        #line=line.lower()
        #line=line.split(',')
        lines.append(line.lower())


words = lines
vectors = []
CV = CountVectorizer(max_features=26,analyzer="char_wb",lowercase=False,ngram_range=(1,26))
tfidf = TfidfVectorizer(max_features=26,analyzer="char_wb",lowercase=False,ngram_range=(1,26))

if VECTOR_TYPE == 1 or VECTOR_TYPE == 2:
    for word in words:
        vectors.append(generate_vector(word, VECTOR_TYPE))
elif VECTOR_TYPE == 3:
    print("Count Vectorizer Reduction :")
    vectors = CV.fit_transform(words).toarray()
else:
    print("Tfidf Vectorizer Reduction :")
    vectors = tfidf.fit_transform(words).toarray()

ktree = WordSearchKDTree(words, vectors)
if ENABLE_RTREE:
    rtree = WordSearchRTree(words, vectors)

print("Enter query word:")
queryWord = input()
if VECTOR_TYPE == 1 or VECTOR_TYPE == 2:
    wordArray = generate_vector(queryWord,VECTOR_TYPE)
elif VECTOR_TYPE == 3:
    rwordArray=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0]
    wordArray = CV.transform(list(queryWord)).toarray()
    for i in wordArray:
        for j in range(0,26):
            if(j==0):
                rwordArray[j]=i[j]
            if(i[j] != 0 and j != 0):
                rwordArray[j]+=i[j]
    wordArray = rwordArray
else:
    rwordArray=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0]
    wordArray = tfidf.transform(list(queryWord)).toarray()
    for i in wordArray:
        for j in range(0,26):
            if(j==0):
                rwordArray[j]=i[j]
            if(i[j] != 0 and j != 0):
                rwordArray[j]+=i[j]
    wordArray = rwordArray


ktree.query(wordArray, TOTAL_NEIGHBORS)
if ENABLE_RTREE:
    rtree.query(wordArray, TOTAL_NEIGHBORS)

if ENABLE_PCA:
    pca = PCA(n_components=PCA_DIMENSION)  

    reduced_vectors = pca.fit_transform(vectors)
    reducedktree = WordSearchKDTree(words, reduced_vectors)
    if ENABLE_RTREE:
        reducedrtree = WordSearchRTree(words, reduced_vectors)
    print("Reduce Dimension")
    reducedWordArray = pca.transform([wordArray])[0]

    reducedktree.query(reducedWordArray, TOTAL_NEIGHBORS)
    if ENABLE_RTREE:
        reducedrtree.query(reducedWordArray, TOTAL_NEIGHBORS)