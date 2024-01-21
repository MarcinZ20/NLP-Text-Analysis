from typing import List

import requests


class Text():

    def __init__(self,
                 text_name: str,
                 text_author: str = 'Unknown',
                 text_file_path: str = None,
                 text_file_url: str = None) -> None:
        self.text_name = text_name
        self.text_author = text_author
        self.text_file_path = text_file_path
        self.text_file_url = text_file_url
        self.words = self.get_words()


    def __repr__(self) -> str:
        return f'Text(text_name={self.text_name}, \\
        text_author={self.text_author}, \\
        text_file_path={self.text_file_path}, \\
        text_file_url={self.text_file_url})'

    def __str__(self) -> str:
        return f'Text: {self.text_name} by {self.text_author}'

    @property
    def text_name(self) -> str:
        return self._text_name

    @text_name.setter
    def text_name(self, text_name: str) -> None:
        if not isinstance(text_name, str):
            raise TypeError('text_name must be a string')
        self._text_name = text_name

    @property
    def text_author(self) -> str:
        return self._text_author

    @text_author.setter
    def text_author(self, text_author: str) -> None:
        if not isinstance(text_author, str):
            raise TypeError('text_author must be a string')
        self._text_author = text_author

    @property
    def text_file_path(self) -> str:
        return self._text_file_path

    @text_file_path.setter
    def text_file_path(self, text_file_path: str) -> None:
        if text_file_path is not None and not isinstance(text_file_path, str):
            raise TypeError('text_file_path must be a string')
        self._text_file_path = text_file_path

    @property
    def text_file_url(self) -> str:
        return self._text_file_url

    @text_file_url.setter
    def text_file_url(self, text_file_url: str) -> None:
        if text_file_url is not None and not isinstance(text_file_url, str):
            raise TypeError('text_file_url must be a string')
        self._text_file_url = text_file_url

    def __get_text(self) -> str:
        """Gets text from a given file path or url

        Returns:
            str: Text
        """
        if self.text_file_path:
            try:
                with open(self.text_file_path, 'r') as f:
                    text = f.read()
            except Exception as e:
                raise Exception(f'Error while getting data from {self.text_file_path}: {e}')
        elif self.text_file_url:
            try:
                r = requests.get(self.text_file_url)
            except Exception as e:
                raise Exception(f'Error while getting data from {self.text_file_url}: {e}')
            
            text = r.text
        else:
            raise Exception('No text file path or url provided')
        
        return text

    def get_words(self) -> List[str]:
        """Gets words from a given file path or url

        Returns:
            List: List of words
        """
        text = self.__get_text()
        text = text.replace('-', ',').replace('=', ',').replace('.', ',')
        lines = text.split('\n')

        words = []

        for line in lines:
            if not line.startswith('#'): # ignore comments
                for word in line.replace(',',' ').split(' '):
                    if len(word):
                        words.append(word.strip())
        return words
    