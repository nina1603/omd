from one_hot_encoder import fit_transform
import pytest


def test_1():
    obtained = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
        ]
    assert obtained == expected


def test_2():
    obtained = fit_transform(
        'I was made for loving you baby you were made for loving me'.split(' ')
    )
    expected = [
         ('I', [0, 0, 0, 0, 0, 0, 0, 0, 1]),
         ('was', [0, 0, 0, 0, 0, 0, 0, 1, 0]),
         ('made', [0, 0, 0, 0, 0, 0, 1, 0, 0]),
         ('for', [0, 0, 0, 0, 0, 1, 0, 0, 0]),
         ('loving', [0, 0, 0, 0, 1, 0, 0, 0, 0]),
         ('you', [0, 0, 0, 1, 0, 0, 0, 0, 0]),
         ('baby', [0, 0, 1, 0, 0, 0, 0, 0, 0]),
         ('you', [0, 0, 0, 1, 0, 0, 0, 0, 0]),
         ('were', [0, 1, 0, 0, 0, 0, 0, 0, 0]),
         ('made', [0, 0, 0, 0, 0, 0, 1, 0, 0]),
         ('for', [0, 0, 0, 0, 0, 1, 0, 0, 0]),
         ('loving', [0, 0, 0, 0, 1, 0, 0, 0, 0]),
         ('me', [1, 0, 0, 0, 0, 0, 0, 0, 0])
    ]
    assert obtained == expected


def test_3():
    obtained = fit_transform('Helloworld'.split(' '))
    expected = [('Helloworld', [1])]
    assert obtained == expected


def test_4():
    obtained = fit_transform('It was the best of times it was the worst of times'.split())
    expected = [
        ('It', [0, 0, 0, 0, 0, 0, 0, 1]),
        ('was', [0, 0, 0, 0, 0, 0, 1, 0]),
        ('the', [0, 0, 0, 0, 0, 1, 0, 0]),
        ('best', [0, 0, 0, 0, 1, 0, 0, 0]),
        ('of', [0, 0, 0, 1, 0, 0, 0, 0]),
        ('times', [0, 0, 1, 0, 0, 0, 0, 0]),
        ('it', [0, 1, 0, 0, 0, 0, 0, 0]),
        ('was', [0, 0, 0, 0, 0, 0, 1, 0]),
        ('the', [0, 0, 0, 0, 0, 1, 0, 0]),
        ('worst', [1, 0, 0, 0, 0, 0, 0, 0]),
        ('of', [0, 0, 0, 1, 0, 0, 0, 0]),
        ('times', [0, 0, 1, 0, 0, 0, 0, 0])
    ]
    assert obtained == expected


def test_exp():
    with pytest.raises(TypeError):
        fit_transform()
