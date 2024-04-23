# Настройки подключения и путь к документации
import configuration

# Предназначен для отправки HTTP-запросов
import requests

# данные пользователя
import data

# Создание заказа

def creat_order(body):
        return requests.post (configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                          json = body)

#  Получение заказа по его номеру трекера
def get_order_from_track(track):
#       get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track}"
        get_order_url_1 = configuration.URL_SERVICE + configuration.FIND_ORDER_FROM_TRACK_PATH + str(track)
#       print(get_order_url)
#       print(get_order_url_1)
        response = requests.get(get_order_url_1)
        return response


# Автотест : Создание заказа:
def test_order_creation_and_retrieval():
        response = creat_order(data.order_body)
#        print(response.text)

# Сохранение номера трека заказа:
        track = response.json()["track"]
#       print("Заказ создан. Номер трека:",track)

# Получение заказа по треку:
        order_response = get_order_from_track(track)

# Проверяется, что код ответа равен 200:
        assert order_response.status_code == 200
        order_data = order_response.json()
#       print("Данные заказа:")
#       print(order_data)


test_order_creation_and_retrieval()






