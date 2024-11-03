# В файле users.json хранится список пользователей с полями:
# имя, возраст, город и профессия. Напишите программу,
# которая считывает файл и выводит только тех пользователей,
# которые старше 30 лет и работают в указанной профессии.
import json

def get_data(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        return json.load(file)

def filter_30_by_profession(data, profession):
    age = 30
    res = list()
    for item in data:
        if int(item["age"]) > age and item["profession"] == profession:
            res.append(item)
    return res

if __name__ == '__main__':

    profession = 'инженер'

    res = filter_30_by_profession(get_data("users.json"), profession)

    for item in res:
        print(f"{item}")

