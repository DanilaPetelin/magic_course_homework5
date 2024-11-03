# Напишите программу, которая сравнивает два JSON-файла
# (file1.json и file2.json) и выводит различия между ними.
# Программа должна определить, какие ключи или значения отличаются.
# Сравнивать только ключи и значения первого уровня.
import json


def get_data(file_name) -> dict:
    with open(file_name, "r", encoding='utf-8') as file:
        return json.load(file)


def find_differences(data_1: dict, data_2: dict):
    different_keys = set(data_1.keys()).symmetric_difference(set(data_2.keys()))
    common_keys = set(data_1.keys()).intersection(set(data_2.keys()))
    different_elem = []

    for item in common_keys:
        if data_1[item] != data_2[item]:
            different_elem.append((item, data_1[item], data_2[item]))

    return different_keys, different_elem


if __name__ == '__main__':
    different_keys, different_elem = find_differences(get_data("file1.json"), get_data("file2.json"))
    print(different_keys)
    print(different_elem)
