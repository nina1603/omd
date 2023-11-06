В модуле test_encoder_pytest.py написаны тесты на fit_transform из модуля one_hot_encoder.py с использованием pytest

Тесты:
1. Преобразование различных текстов и массивов строк
2. Проверка выброса исключения

pytest -vq test_encoder_pytest.py

В модуле test_encoder_unittest.py написаны тесты на fit_transform из модуля one_hot_encoder.py с использованием unittest

Тесты:
1. Преобразование текста и массивов строк
2. Проверка на неравенство результатов для строк, отличающихся одним словом
3. Проверка выброса исключения
4. Проверка пустого ввода

python -m unittest -v test_encoder_unittest.TestFitTransform.test_1
python -m unittest -v test_encoder_unittest.TestFitTransform.test_2
python -m unittest -v test_encoder_unittest.TestFitTransform.test_3
python -m unittest -v test_encoder_unittest.TestFitTransform.test_4
python -m unittest -v test_encoder_unittest.TestFitTransform.test_5
python -m unittest -v test_encoder_unittest.TestFitTransform.test_6
python -m unittest -v test_encoder_unittest.TestFitTransform.test_exp