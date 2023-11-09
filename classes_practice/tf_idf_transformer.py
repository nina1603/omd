import numpy as np
from count_vectorizer import CountVectorizer


class TdidfTransformer:
    @staticmethod
    def tf_transform(matrix: list) -> list:
        """
        counts tf for all words in the corpus
        :param matrix: list of term vectors
        :return: list of tf-values - importance of the term
        """
        tf_matrix = [[] for _ in matrix]
        sums_ = [sum(it) for it in matrix]
        for i, vector in enumerate(matrix):
            tf_matrix[i] = [round(scalar / sums_[i], 3) for scalar in vector]
        return tf_matrix

    @staticmethod
    def idf_transform(matrix: list) -> list:
        """
        counts idf for all words in the corpus
        :param matrix: list of term vectors
        :return: list of idf-values - frequence inversion of the term
        """
        matrix = np.array(matrix).astype(bool)
        sums_ = matrix.sum(axis=0)
        len_ = len(matrix)
        idf_matrix = np.round(np.log((len_ + 1) / (sums_ + 1)) + 1, 2)
        return idf_matrix

    def fit_transform(self, count_matrix: list) -> list:
        """
        performs both tf and idf (multiplies them to get the final result)
        :param count_matrix: list of term vectors
        :return: the product of tf and idf for each term in corpus
        """
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        res = []
        for doc in tf:
            res.append([round(t * i, 3) for t, i in zip(doc, idf)])
        return res


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tfidf = TdidfTransformer()

    def fit_transform(self, corpus: list) -> list:
        """
        gets the corpus and vectorizes it, then counts tf-idf for each word
        :param corpus: the term corpus (documents)
        :return: tf-idf values for each term in the corpus
        """
        count_matrix = super().fit_transform(corpus)
        return self.tfidf.fit_transform(count_matrix)


if __name__ == '__main__':
    count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    transformer = TdidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(f"tf-idf matrix: {tfidf_matrix}")

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print("Vectorizer features:")
    print(vectorizer.get_feature_names())