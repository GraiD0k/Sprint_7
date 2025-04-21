import requests
from data.urls import Urls
import allure

class CreateOrdersApi:
    @staticmethod
    @allure.step('Вызываем метод создания заказа')
    def post_create_order(first_name,last_name,address,metro_station,phone,rent_time,delivery_date,comment,color):
        payload = {
    "firstName": first_name,
    "lastName": last_name,
    "address": address,
    "metroStation": metro_station,
    "phone": phone,
    "rentTime": rent_time,
    "deliveryDate": delivery_date,
    "comment": comment,
    "color": [
        color
    ]
}
        response = requests.post(Urls.URL_CREATE_ORDERS,json=payload)
        return response