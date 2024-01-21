from collections import Counter, OrderedDict
from pathlib import Path
from typing import Dict, List, Tuple

from models.text import Text


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
    
    def __generate_n_grams(self, number: int) -> List[str]:
        """Helper function that generates n-grams for a given number

        Args:
            number (int): n-gram

        Returns:
            List[str]: List of n-grams
        """

        grams = []
        len_words = len(self.text.words)

        for i in range(len_words - number+1):
            gram = ' '.join(self.text.words[i : i+number])
            grams.append(gram)

        return grams
    
    def calculate_n_grams(self, n_start: int = 2, n_end: int = 4) -> List[Dict]:
        """Function to calculate n-grams for the provided text

        Args:
            n_start (int, optional): start index. Defaults to 2.
            n_end (int, optional): end index. Defaults to 3.

        Returns:
            List[Dict]: List of n-grams as dictionaries
            ex.: [{gram: n}, ...]
        """

        if n_start < 1:
            raise Exception('Starting index cannot be lower than 2')
        
        if n_end > 10:
            raise Exception('End index cannot be greater than 10')

        n_grams: List = []
        
        for n in range(n_start, n_end):
            grams = self.__generate_n_grams(n)
            g = dict(Counter(grams).most_common())

            n_grams.append(g)

        return n_grams

class ZipfPrinter:
    """A class for plotting Zipf's Law graph and analyzing n-grams and collocations

    Args:
        text (Text): choosen text
        word_ranks (List): List of word ranks
        word_frequencies (List): List of word frequencies

    Methods:
        print_n_grams: Prints n-grams
        print_collocations: Prints collocations
    """

    def __init__(self, text: Text, words_ranks: List, word_frequencies: List, n_grams: List[Dict], use_writer: bool = True) -> None:
        self.text = text
        self.words_ranks = words_ranks
        self.word_frequencies = word_frequencies
        self.n_grams = n_grams
        self.use_writer = use_writer

    def print_n_grams_result(self, start_index: int = 2) -> None:
        print('\n\n- - - - - N-GRAMS ANALYSIS - - - - -\n')

        for index, n_gram in enumerate(self.n_grams):
            print(f'\n{index + start_index}-GRAMs')
            print('---------')

            for key, value in n_gram.items():
                if value > 1:
                    print(f'{key}: {value}')

        if self.use_writer:
            writer = ZipfWriter(self.text)
            writer.write_n_grams_result(self.n_grams)

    def print_collocations_result(self) -> None:
        print('- - - - - COLLOCATIONS ANALYSIS - - - - -\n')

        unique_words = list(set(self.text.words))
        collocations = {unique_word: [] for unique_word in unique_words}

        for i in range(len(self.text.words) - 1):
            collocations[self.text.words[i]].append(self.text.words[i+1])

        for key, value in collocations.items():
            print(f'{key} occurs in {len(set(value))} collocations\t')

        if self.use_writer:
            writer = ZipfWriter(self.text)
            writer.write_collocations_result(collocations)

class ZipfWriter:
    """A class for writing Zipf's Law analysis results to a text file
    """

    def __init__(self, text: Text) -> None:
        self.text = text
        self.output_path = "data/output/"

    def write_n_grams_result(self, n_grams: List[Dict], start_index: int = 2) -> None:
        """Writes n-grams analysis result to a text file in data/output folder

        Args:
            n_grams (List): List of n-grams

        Returns:
            None
        """

        file_name = f"{self.text.text_name.replace(' ', '_')}_n_grams_result.txt"
        file_path = Path(self.output_path + file_name).absolute()

        if not file_path.exists():
            file_path.touch()

        with open(file_path, 'w') as f:
            f.write(f'N-grams analysis for "{self.text.text_name}" by {self.text.text_author}\n')

            for index, n_gram in enumerate(n_grams):
                print(type(n_gram))
                f.write(f'\n{index + start_index}-GRAMs\n--------\n')

                for key, value in n_gram.items():
                    if value > 1:
                        f.write(f'{key}: {value}\n')

            f.write('\n\n')

    def write_collocations_result(self, collocations: Dict) -> None:
        """Writes collocations analysis result to a text file

        Args:
            collocations (Dict): Dictionary of collocations

        Returns:
            None
        """

        file_name = f"{self.text.text_name.replace(' ', '_')}_collocations_result.txt"
        file_path = Path(self.output_path + file_name).absolute()

        if not file_path.exists():
            file_path.touch()

        with open(file_path, 'w') as f:
            f.write(f'Collocations analysis for "{self.text.text_name}" by {self.text.text_author}\n\n')

            for key, value in collocations.items():
                f.write(f'{key} occurs in {len(set(value))} collocations\n')

            f.write('\n\n')


        