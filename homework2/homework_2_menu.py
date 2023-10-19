import csv
import os

# пути к источнику данных и к результирующему файлу
input_data_path = './data/Corp_Summary.csv'
output_data_path = './data/department_info.csv'

def menu(input_path = input_data_path, output_path = output_data_path) -> None:
    """
    Основное меню, в котором выбирается нужная опция и выполняется действие
    :params
        input_path - путь к файлу с источником данных
        output_path - путь к файлу, куда записывать результат
    """
    option = ''
    options = ['1', '2', '3']
    while option not in options:
        print(
            f'Выберите опцию: 1, 2 или 3, где:\n'
            f'1. Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него\n'
            f'2. Вывести сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату\n'
            f'3. Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. При этом необязательно вызывать сначала команду из п.2'
        )
        option = input()
    if option == '1':
        first_option(input_path)
    elif option == '2':
        second_option(input_path)
    else:
        third_option(input_path, output_path)

def get_data(
    filepath: str, delim: str = ';',
    sort_items: tuple = tuple(['Департамент', 'Отдел'])
    ) -> list:
    """
    Получает данные из файла в виде отсортированного списка словарей
    :param
        filepath - путь к источнику данных
        delim - символ-разделитель
        sort_items - ключ - один или несколько столбцов - для сортировки данных
    :return
        data - сортированный по sort_items список словарей с данными из источника
    """
    with open(filepath, encoding='utf-8') as file:
        data = list(csv.DictReader(file, delimiter=delim))
        data = sorted(data, key=lambda k: tuple(k[item] for item in sort_items))
    return data

def first_option(input_path) -> None:
    """
    Вывести в понятном виде иерархию команд, т.е. департамент и все команды,
    которые входят в него
    :params
        input_path - путь к файлу с источником данных
    """
    department_teams = {}
    # получение данных из источника
    data = get_data(input_path)
    for element in data:
        dep, team = element['Департамент'], element['Отдел']
        # для каждого департмента создаём множество его отделов - без повторов
        if dep not in department_teams.keys():
            department_teams[dep] = {team}
        else:
            department_teams[dep].add(team)
    print('Департаменты и команды в них:')
    for key, val in department_teams.items():
        print(key, end = ': ')
        print(*val, sep=', ', end='.\n')

def get_report(input_path) -> dict:
    """
    Создать сводку по статистике зарплат по департаментам
    :params
        input_path - путь к файлу с источником данных
    :return
        report - словарь словарей с данными, групированными по департаменту
    """
    # получение данных из источника
    data = get_data(input_path)
    # создание словаря с информацией по департаментам
    report = {}
    salaries = {}
    for element in data:
        dep, salary = element['Департамент'], int(element['Оклад'])
        if dep not in salaries.keys():
            salaries[dep] = [salary]
        else:
            salaries[dep].append(salary)
    for department, salary_list in salaries.items():
        report[department] = {
            'Численность': len(salary_list),
            'Вилка минимальная': min(salary_list),
            'Вилка максимальная': max(salary_list),
            'Средняя зарплата': round(sum(salary_list) / len(salary_list), 1)
            }
    return report

def second_option(input_path) -> None:
    """
    Вывести сводный отчёт по департаментам: название, численность,
    "вилка" зарплат в виде мин – макс, среднюю зарплату
    :params
        input_path - путь к файлу с источником данных
    """
    report = get_report(input_path)
    print('Статистика по зарплатам в департаментах:')
    for key, val in report.items():
        print(f"*{key}*.")
        print(
            *[f'{metric}: {value}' for metric, value in report[key].items()],
            sep = ',\t', end=".\n"
        )

def third_option(input_path, output_path) -> None:
    """
    Сохранить сводный отчёт из предыдущего пункта в виде csv-файла.
    При этом необязательно вызывать сначала команду из п.2
    :params
        input_path - путь к файлу с источником данных
        output_path - путь к файлу со сводной таблицей по зарплатами
    """
    report = get_report(input_path)
    if os.path.isfile(output_path):
        print(f"Результаты уже были сохранены в {output_path}")
    else:
        # перепишем данные в виде списка словарей, чтобы записать в csv
        csv_format_report = []
        for dep, stats_info in report.items():
            row = dict({'Департамент': dep})
            stats = {metric: value for metric, value in stats_info.items()}
            row.update(stats)
            csv_format_report.append(row)
        # запись в файл
        with open(output_path, encoding='utf-8', mode='w') as f:
            w = csv.DictWriter(
                f,
                fieldnames=[name for name in csv_format_report[0].keys()],
                delimiter=";"
            )
            w.writeheader()
            for element in csv_format_report:
                w.writerow(element)
        print(f"Результаты сохранены в {output_path}")

if __name__ == '__main__':
    menu()