class CountVectorizer:
    def __init__(self):
        self.extra_symbols = '!"#$%&()*+, -./:;<=>?@[\]^_`{|}~'
        self.corpus = None

    def fit_transform(self, corpus) -> list:
        """
        Learn the vocabulary dictionary and return document-term matrix.
        :param corpus - the corpus of documents is required for constructing tf-idf matrix
        :return term_matrix - list of lists - tf-idf matrix for corpus
        """
        self.corpus = corpus
        # len_ = len(corpus)
        word_counters = [self.get_word_counts(text) for text in corpus]
        term_matrix = [[] for _ in corpus]

        feature_names = self.get_feature_names()
        for word in feature_names:
            for i, counter in enumerate(word_counters):
                term_matrix[i].append(counter.get(word, 0))
        return term_matrix

    def get_feature_names(self, corpus=None) -> list:
        """
        Get output feature names for transformation
        :param corpus - if fit_transform wasn't launched then the corpus of documents is required for analysis
        :return vocabulary - list of unique words (list, not set, for keeping the order of appearance)
        """
        if self.corpus is None:
            if corpus is not None:
                self.corpus = corpus
            else:
                raise ValueError(f"The word corpus wasn't given and fit_transform still hasn't been launched!")
        lowerize_corpus = ' '.join(self.corpus).lower().split()
        vocabulary = []
        for word in lowerize_corpus:
            word = word.strip(self.extra_symbols)
            if word not in vocabulary:
                vocabulary.append(word)
        return vocabulary

    def get_word_counts(self, text: str) -> dict:
        """
        for a particular text counts all the words inside it
        :param text - initial text from document
        :return word_counter - dictionary with count of each word appearance in the text
        """
        word_counter = {}
        words = text.lower().split()
        for word in words:
            word_counter.setdefault(word, 0)
            word_counter[word] += 1
        return word_counter