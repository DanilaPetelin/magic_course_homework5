# Напишите программу, которая считывает данные из
# CSV-файла sales.csv, где содержатся данные о продажах
# (например, дата, товар, количество, цена).
# Программа должна вывести:
# - Общую сумму продаж.
# - Товар с наибольшим числом продаж.
import csv

with open("sales.csv", 'r', encoding='utf-8') as f:
    data = csv.DictReader(f)

    amount = 0
    max_sold_quntity = 0
    max_sold_product_name = set()

    for item in data:
        qu= int(item.get('quantity'))
        pr = float(item.get('price'))
        amount +=qu*pr
        if qu > max_sold_quntity:
            max_sold_quntity =qu
            max_sold_product_name = set()
            max_sold_product_name.add(item.get('product'))
        elif qu == max_sold_quntity:
            max_sold_product_name.add(item.get('product'))

    print(amount)
    print(max_sold_product_name)


