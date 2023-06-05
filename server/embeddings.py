"""
`embeddings.py` is used for working with pre-trained word embeddings. 
It can be helpful in various Natural Language Processing (NLP) tasks. 
Word embeddings map words to high-dimensional vectors such that semantically 
similar words are mapped to nearby points.

One interesting property of word embeddings is that they can capture semantic 
relationships between words: for example, the analogy "king is to man as queen is to woman" 
corresponds to a particular spatial relationship in the vector space. You can even use
vector arithemtic in embedding space: given their vectors, "king" - "man" + "queen" = "woman".

The script provides a utility for finding the closest words to a given word, 
as well as for solving word analogies. For instance, given the words 'man', 'he', and 'woman',
 it finds the word that stands in the same relationship to 'woman' as 'he' does to 'man'.
"""

from annoy import AnnoyIndex
import numpy as np

class PreTrainedEmbeddings:
    """ A wrapper around pre-trained word vectors and their use """
    def __init__(self, word_to_index, word_vectors):
        """
        Initialize an instance with given word-to-index mapping and word vectors.
        Construct an inverse index for easy lookup and prepare AnnoyIndex for nearest neighbor search.

        Args:
            word_to_index (dict): mapping from word to integers
            word_vectors (list of numpy arrays)
        """

        # word_to_index and word_vectors are the core data structures
        self.word_to_index = word_to_index
        self.word_vectors = word_vectors
        # inverse index to look up words using their vector indices
        self.index_to_word = {v: k for k, v in self.word_to_index.items()}

        # setting up the Annoy index for fast nearest neighbor search
        self.index = AnnoyIndex(len(word_vectors[0]), metric='euclidean')
        print("Building Index!")
        # Adding all word vectors to the Annoy index
        for _, i in self.word_to_index.items():
            self.index.add_item(i, self.word_vectors[i])
        # Building the index
        self.index.build(50)
        print("Finished!")
        
    @classmethod
    def from_embeddings_file(cls, embedding_file):
        """
        Class method to create an instance of PreTrainedEmbeddings from a file of pre-trained vectors.

        Vector file should be of the format:
            word0 x0_0 x0_1 x0_2 x0_3 ... x0_N
            word1 x1_0 x1_1 x1_2 x1_3 ... x1_N
        
        Args:
            embedding_file (str): location of the file
        Returns: 
            instance of PretrainedEmbeddings
        """
        
        word_to_index = {}
        word_vectors = []

        with open(embedding_file) as fp:
            for line in fp.readlines():
                line = line.split(" ")
                word = line[0]
                vec = np.array([float(x) for x in line[1:]])
                
                word_to_index[word] = len(word_to_index)
                word_vectors.append(vec)
                
        # Create an instance with the word_to_index map and the word vectors list.
        return cls(word_to_index, word_vectors)
    
    def get_embedding(self, word):
        """
        Method to retrieve the vector embedding of a word.

        Args:
            word (str)
        Returns
            an embedding (numpy.ndarray)
        """
        return self.word_vectors[self.word_to_index[word]]

    def get_closest_to_vector(self, vector, n=1):
        """
        Given a vector, find the n closest vectors in the embedding space using the Annoy index.
        Return the corresponding words.

        Args:
            vector (np.ndarray): should match the size of the vectors 
                in the Annoy index
            n (int): the number of neighbors to return
        Returns:
            [str, str, ...]: words that are nearest to the given vector. 
                The words are not ordered by distance 
        """
        nn_indices = self.index.get_nns_by_vector(vector, n)
        return [self.index_to_word[neighbor] for neighbor in nn_indices]
    
    def compute_analogy(self, word1, word2, word3):
        """
        Given an analogy of the form word1:word2 as word3:?, compute the vector for ? and find the closest
        words in the embedding space. Return these words.

        Args:
            word1 (str)
            word2 (str)
            word3 (str)

        Returns:
            List[str]: top 4 most likely answers
        """
        try:
            vec1 = self.get_embedding(word1.lower())
            vec2 = self.get_embedding(word2.lower())
            vec3 = self.get_embedding(word3.lower())
        except KeyError as e:
            print("Word not found in vocabulary: ", e)
            return ['Invalid word']

        # Compute the vector that completes the analogy
        spatial_relationship = vec2 - vec1
        vec4 = vec3 + spatial_relationship

        # Find the closest words to vec4 in the embedding space
        closest_words = self.get_closest_to_vector(vec4, n=4)
        # Exclude the input words from the closest words
        existing_words = set([word1, word2, word3])
        closest_words = [word for word in closest_words 
                             if word not in existing_words] 

        # If no closest words are found, print a message and return an empty list
        if len(closest_words) == 0:
            print("Could not find nearest neighbors for the computed vector!")
            return ['No similar words']

        return closest_words

# Load pre-trained embeddings from the specified file
embeddings = PreTrainedEmbeddings.from_embeddings_file('data/glove/glove.6B.100d.txt')

# Check if the script is being executed directly
if __name__ == '__main__':
    # Define a list of input word analogies
    inputs = [
        ('man', 'he', 'woman'),
        ('fly', 'plane', 'sail'),
        ('cat', 'kitten', 'dog'),
        ('blue', 'color', 'dog'),
        ('leg', 'legs', 'hand'),
        ('toe', 'foot', 'finger'),
        ('talk', 'communicate', 'read'),
        ('blue', 'democrat', 'red'),
        ('man', 'king', 'woman'),
        ('man', 'doctor', 'woman'),  # nurse: gender bias in NLP embeddings
        ('fast', 'fastest', 'small'),
    ]

    # Iterate over each input analogy
    for (w1, w2, w3) in inputs:
        # Compute possible word analogies for w4 based on w1, w2, and w3
        possible_w4 = embeddings.compute_analogy(w1, w2, w3)
        
        # Iterate over each possible word analogy
        for w4 in possible_w4:
            # Print the analogy in the format: w1 : w2 :: w3 : w4
            print("{} : {} :: {} : {}".format(w1, w2, w3, w4))
