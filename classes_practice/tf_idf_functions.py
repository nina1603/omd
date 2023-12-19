import numpy as np

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


def idf_transform(matrix: list) -> list:
    """
    counts idf for all words in the corpus
    :param matrix: list of term vectors
    :return: list of idf-values - frequency inversion of the term
    """
    matrix = np.array(matrix).astype(bool)
    sums_ = matrix.sum(axis=0)
    len_ = len(matrix)
    idf_matrix = np.round(np.log((len_ + 1) / (sums_ + 1)) + 1, 2)
    return idf_matrix

def idf_transform_alternative(count_matrix: list) -> list:
    """
    just another way of count idf for all words in the corpus
    :param matrix: list of term vectors
    :return: list of idf-values - frequency inversion of the term
    """
    count_np = np.array(count_matrix)
    count_np[count_np > 0] = 1
    idf = np.log((count_np.shape[0] + 1) / (count_np.sum(axis = 0) + 1)) + 1
    return np.around(idf, 3)

def idf_transform_simple(count_matrix : list) -> list:
    """
    again, just another way of count idf for all words in the corpus
    :param count_matrix: list of term vectors
    :return: list of idf-values - frequency inversion of the term
    """
    idfs = []
    total_docs = len(count_matrix)
    total_words = len(count_matrix[0])
    for i in range(total_words):
        docs_i = 0
        for doc in count_matrix:
            if doc[i] > 0:
                docs_i += 1
        idfs.append(np.around(np.log((total_docs + 1)/(docs_i + 1)) + 1, 3))
    return idfs

def tf_idf(count_matrix: list) -> list:
    """
    performs both tf and idf (multiplies them to get the final result)
    :param count_matrix: list of term vectors
    :return: the product of tf and idf for each term in corpus
    """
    tf = tf_transform(count_matrix)
    idf = idf_transform(count_matrix)
    res = []
    for doc in tf:
        res.append([t * i for t, i in zip(doc, idf)])
    return res

if __name__ == '__main__':
    count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

    tf_matrix = tf_transform(count_matrix)
    print(f"tf: {tf_matrix}")

    idf_matrix = idf_transform(count_matrix)
    print(f"idf: {idf_matrix}")