from scipy.spatial import KDTree
import numpy as np
import time

class WordSearchKDTree:
    def __init__(self, words, vectors):
        vector_array = np.array(vectors)
        self.tree = KDTree(vector_array)
        self.words = words

    def query(self, wordArray, count):
        start = time.time()
        distances, indices = self.tree.query(wordArray, k=count)
        end = time.time()
        print("Query time of the k-tree is- ", end-start)

        result = []
        for index in indices:
            result.append(self.words[index])

        print(result)