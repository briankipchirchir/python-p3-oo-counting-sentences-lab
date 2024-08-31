#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        """
        Initialize the MyString class with a value.
        :param value: The string value (default is an empty string).
        """
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError("Value must be a string")
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        """
        Check if the value is a sentence (ends with a period).
        :return: True if the value ends with '.', False otherwise.
        """
        return self.value.endswith('.')

    def is_question(self):
        """
        Check if the value is a question (ends with a question mark).
        :return: True if the value ends with '?', False otherwise.
        """
        return self.value.endswith('?')

    def is_exclamation(self):
        """
        Check if the value is an exclamation (ends with an exclamation mark).
        :return: True if the value ends with '!', False otherwise.
        """
        return self.value.endswith('!')

    def count_sentences(self):
        """
        Count the number of sentences in the value.
        A sentence ends with '.', '!', or '?'.
        :return: The number of sentences.
        """
        # Replace multiple punctuation marks with a single period.
        cleaned_value = re.sub(r'[.!?]+', '.', self.value)
        # Split the string into sentences using the period.
        sentences = cleaned_value.split('.')
        # Filter out empty strings.
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)

