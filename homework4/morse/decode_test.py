"""Morse Code Translator"""
from morse import MORSE_TO_LETTER


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    >>> decode(' ')
    ''
    >>> decode('Hello world!') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    KeyError: 'Hello'
    >>> decode('.')
    'E'
    >>> decode('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.')
    'MAI-PYTHON-2019'
    >>> decode('- . ... -')
    'TEST'
    >>> decode('... --- ...')
    'SOS'
    >>> decode('..  -....- .-.. .. -.- . -....-  -.-. .- -.- . ...')
    'I-LIKE-CAKES'
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


if __name__ == '__main__':
    morse_msg = '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'
    decoded_msg = decode(morse_msg)
    print(f"Decoded: {decoded_msg}")
