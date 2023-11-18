В модуле encode_test.py тестируется функция encode().

Запуск: 

python -m doctest -o NORMALIZE_WHITESPACE -v encode_test.py

Тесты:

1. ''
2. 'SOS'
3. 'HELLO WORLD' (с / без директивы)
4. 'Hello world' (exception)

Результат: все тесты пройдены

В модуле decode_test.py тестируется функция decode().

Запуск: 

python -m pytest -q ./morse/decode_test.py::test_decode

Тесты:

1. ' '
2. '.'
3. 'Hello world!' (exception)
4. '... --- ...'

Результат: все тесты пройдены