from rtree import index
import time

class WordSearchRTree:
    def __init__(self, words, vectors):
        p = index.Property()
        p.dimension = len(vectors[0])  
        self.idx = index.Index(properties=p)
        for i, value in enumerate(vectors):
            self.idx.insert(i, tuple(value))
        self.words = words


    def query(self, wordArray, count):
        start = time.time()
        indices = self.idx.nearest(tuple(wordArray), count)
        end = time.time()
        print("Query time of the r-tree is- ", end-start)
        result = []

        for index in indices:
            result.append(self.words[index])
            if len(result) >= count:
                break

        print(result)



