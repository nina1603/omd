Запуск тестов: 

python3 -m pytest -v -s what_is_year_now_test.py

С покрытием:

python -m pytest -q what_is_year_now_test.py --cov=letters_counter

Отчёт в html:

python -m pytest --cov . --cov-report html