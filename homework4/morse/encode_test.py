"""Morse Code Translator"""
from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответствии с таблицей азбуки Морзе
    >>> encode('')
    ''
    >>> encode('SOS')
    '... --- ...'
    >>> encode('HELLO WORLD')
    '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'
    >>> encode('HELLO WORLD') # doctest: +ELLIPSIS
    '.... ... .-.. -..'
    >>> encode('Hello world') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    KeyError: 'e'
    """

    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


if __name__ == '__main__':
    msg = 'I LIKE CAKES'
    print(f"Encoded: {encode(msg)}")
