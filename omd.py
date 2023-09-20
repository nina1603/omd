import random

# Guido van Rossum <guido@python.org>
def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return ()

def step2_umbrella():
    v = random.randint(15, 30)
    print(
        f'Утка взяла зонтик и вышла на улицу. Скорость ветра достигла {v} метров в секунду.'
        f'Утку унесло на зонтике прямо в пруд, и она решила, что лучше останется в нём, потому что оттуда открывался хороший вид.'
    )

def step2_no_umbrella():
    print(f'Утка сильно промокла под дождём, но затем выпила в баре и согрелась. Наутро она не пошла на работу и осталась релаксить в кровати.')