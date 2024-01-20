from collections import Counter, OrderedDict
from pprint import pprint
from typing import List, Tuple, Dict

import matplotlib.pyplot as plt

from src.models.text import Text


class ZipfAnalyzer:
    """Class for Zipf's Law analysis

    Args:
        text_name (str): Name of the text
    
    Methods:
        calc_zipf_law_properties: Calculates Zipf's Law properties for a given list of words

        get_words_from_url: Gets words from a given url

        get_words_from_file: Gets words from a given file

        plot_zipf_law: Plots Zipf's Law graph
    """

    def __init__(self, text: Text) -> None:
        self.text = text

    def calc_zipf_law_properties(self) -> Tuple[range, List[int]]:
        """Calculates Zipf's Law properties for a given list of words

        Args:
            words (List): List of words

        Returns:
            Tuple[list, list]: Tuple of word ranks and word frequencies
        """
        words_count = Counter(self.text.words)
        sorted_words_count = sorted(words_count.items(), 
                                    key=lambda x: x[1], 
                                    reverse=True)

        word_ranks = range(1, len(sorted_words_count) + 1)
        word_frequencies = [count for _, count in sorted_words_count]

        return word_ranks, word_frequencies
    
    def generate_n_grams(self, n: int) -> List[str]:
        """Generates n-grams for a given list of words

        Args:
            words (List[str]): List of words
            n (int): n-gram

        Returns:
            List[str]: List of n-grams
        """

        grams = []

        for i in range(len(self.text.words) - n+1):
            grams.append(' '.join(self.text.words[i:i+n]))

        return grams


class ZipfPlotter:
    """A class for plotting Zipf's Law graph and analyzing n-grams and collocations

    Args:
        word_ranks (List): List of word ranks
        word_frequencies (List): List of word frequencies
        text_name (str): Name of the text

    Methods:
        print_n_grams: Prints n-grams

        print_collocations: Prints collocations

        plot_zipf_law: Plots Zipf's Law graph
    """

    def __init__(self, text: Text, words_ranks: List, word_frequencies: List) -> None:
        self.text = text
        self.words_ranks = words_ranks
        self.word_frequencies = word_frequencies

    def print_n_grams_result(self) -> None:
        print('\nN-GRAMS ANALYSIS')

        grams = ZipfAnalyzer.generate_n_grams(self.text.words, 2)

        for r in range(2, 10):
            print(f'\n{r}-grams: ')

            g = OrderedDict(Counter(grams).most_common())

            for k in g.keys():
                if g[k] > 1:
                    print(f'{k}: {g[k]}')

    def print_collocations_result(self) -> None:
        print('Collocations (graph) analysis')

        unique_words = list(set(self.text.words))
        collocations = {unique_word: [] for unique_word in unique_words}

        for i in range(len(self.text.words) - 1):
            collocations[self.text.words[i]].append(self.text.words[i+1])

        pprint(collocations, sort_dicts=False)

        for k, v in collocations.items():
            print(f'{k} occurs in {len(set(v))} collocations\t')

    def plot_zipf_law(self) -> None:
        """Plots Zipf's Law graph

        Returns:
            None
        """
        plt.figure(figsize=(20, 10))

        plt.plot(self.words_ranks, 
                 self.word_frequencies, 
                 color='magenta')
        
        plt.xlabel('Words Ranks')
        plt.ylabel('Words Frequencies')
        plt.title(f'Zipf Law for "{self.text.text_name}" by {self.text.author}')

        plt.show()


class ZipfWriter:
    """A class for writing Zipf's Law analysis results to a text file
  """
    def __init__(self, text: Text) -> None:
        self.text = text

    def write_zipf_law_result(self, word_ranks: List, word_frequencies: List) -> None:
        """Writes Zipf's Law analysis result to a text file

        Args:
            word_ranks (List): List of word ranks
            word_frequencies (List): List of word frequencies

        Returns:
            None
        """
        with open(f'../data/output/{self.text.text_name}_zipf_law_result.txt', 'w') as f:
            f.write(f'Zipf Law for "{self.text_name}" by {self.author}\n\n')
            f.write('Word Ranks\tWord Frequencies\n')

            for i in range(len(word_ranks)):
                f.write(f'{word_ranks[i]}\t{word_frequencies[i]}\n')

            f.write('\n\n')

    def write_n_grams_result(self, n_grams: List) -> None:
        """Writes n-grams analysis result to a text file

        Args:
            n_grams (List): List of n-grams

        Returns:
            None
        """
        with open(f'../data/output/{self.text_name}_n_grams_result.txt', 'w') as f:
            f.write(f'N-grams analysis for "{self.text_name}" by {self.author}\n\n')

            for n_gram in n_grams:
                f.write(f'{n_gram}\n')

            f.write('\n\n')

    def write_collocations_result(self, collocations: Dict) -> None:
        """Writes collocations analysis result to a text file

        Args:
            collocations (Dict): Dictionary of collocations

        Returns:
            None
        """

        with open(f'../data/output/{self.text_name}_collocations_result.txt', 'w') as f:
            f.write(f'Collocations analysis for "{self.text_name}" by {self.author}\n\n')

            for k, v in collocations.items():
                f.write(f'{k}: {v}\n')

            f.write('\n\n')


        