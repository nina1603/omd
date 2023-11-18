from one_hot_encoder import fit_transform
import unittest

class TestFitTransform(unittest.TestCase):
    def test_1(self):
        obtained = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEquals(obtained, expected)

    def test_2(self):
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
        self.assertEquals(obtained, expected)

    def test_3(self):
        obtained = fit_transform('Helloworld'.split(' '))
        expected = [('Helloworld', [1])]
        self.assertEquals(obtained, expected)


    def test_4(self):
        obtained_1 = fit_transform('It was the best of times it was the worst of times'.split())
        obtained_2 = fit_transform('it was the best of times it was the worst of times'.split())

        self.assertNotEqual(obtained_1, obtained_2)

    def test_5(self):
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

        self.assertEqual(obtained, expected)

    def test_6(self):
        obtained = fit_transform(' '.split())
        self.assertFalse(obtained)

    def test_exp(self):
        with self.assertRaises(TypeError) as context:
            fit_transform()
        self.assertTrue('expected at least 1 arguments, got 0' in str(context.exception))
