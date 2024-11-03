# Система учета заказов

# У вас есть JSON-файл orders.json,
# содержащий данные о заказах интернет-магазина.
# Каждый заказ включает информацию о клиенте,
# заказанных товарах, количестве и цене.

# Напишите программу, которая:
# Выводит общую сумму каждого заказа.
# Находит клиента с наибольшей суммой заказа и выводит его имя и сумму.
import json

with open("orders.json", "r", encoding='utf-8') as file:
    data =  json.load(file)
    max_order_name = list()
    max_order_amount = 0

    for order in data["orders"]:
        order_amount = 0
        for item in order["items"]:
            order_amount += item["quantity"]*item["price"]
        print(f'Сумма заказа с id {order["order_id"]}   {order_amount}')
        if order_amount > max_order_amount:
            max_order_amount =order_amount
            max_order_name = [order["customer"]["name"]]
        elif order_amount == max_order_amount:
            max_order_name.append(order["customer"]["name"])

    print(f"максимальная сумма заказа равна {max_order_amount}, клиенты: {max_order_name}")



