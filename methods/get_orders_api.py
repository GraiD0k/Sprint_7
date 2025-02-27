import requests
from data.urls import Urls
import allure

class GetOrdersApi:
    @staticmethod
    @allure.step('Вызываем метод получения заказов')
    def get_orders():
        response = requests.get(Urls.URL_GET_ORDERS)
        return response