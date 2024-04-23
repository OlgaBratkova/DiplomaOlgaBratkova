# заголовки для HTTP-запроса, указывающие на то, что тело запроса
# будет в формате JSON
import requests

headers = {
    "Content-Type": "application/json"
}

# данные пользователя для создания заказа
# содержат имя,фамилия,адрес пользователя,станция метро,номер телефона
# дата доставки, цвет,комментарий.
order_body = {
            "firstName": "Irina",
            "lastName": "Ivanova",
            "address": "Arbat",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-04-25",
            "comment": "call ahead",
            "color": ["BLACK"]
                }





