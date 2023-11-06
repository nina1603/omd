"""Morse Code Translator"""
import pytest
from morse import MORSE_TO_LETTER, decode


@pytest.mark.parametrize(
    "input_, expected",
    [
        pytest.param(
             ' ', '', id="first"
        ),
        pytest.param(
             '.', 'E', id="second"
        ),
        pytest.param(
             'Hello world!', pytest.raises(KeyError), id="third",
        ),
        pytest.param(
             '... --- ...', 'SOS', id="fourth"
        ),
    ],
)
def test_decode(input_: str, expected: str):
    try:
        obtained = decode(input_)
        assert obtained == expected
    except KeyError:
        with pytest.raises(KeyError) as exc_info:
            obtained = decode(input_)
            assert str(exc_info.value) == obtained


if __name__ == '__main__':
    test_decode()
