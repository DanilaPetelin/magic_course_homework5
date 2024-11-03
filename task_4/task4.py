#   В файле employees.csv содержится список сотрудников
# с полями: имя, возраст, должность, зарплата.
# Напишите программу, которая считывает данные
# и выводит только тех сотрудников,
# у которых зарплата больше 50,000.
import csv

SALARY_LIMIT =50000
with open("employees.csv", 'r', encoding='utf-8') as f:
    data = csv.DictReader(f)

    for item in data:
        if float(item.get('salary')) > SALARY_LIMIT:
            print(item)