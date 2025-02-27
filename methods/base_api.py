import requests
from data.urls import Urls
import allure

class BaseApi:
    @staticmethod
    @allure.step('Вызываем метод создания курьера')
    def post_create_courier(login,password,first_name):
        payload = {"login":login,"password":password,"firstName":first_name}
        response = requests.post(Urls.URL_CREATE_COURIER,data=payload)
        return response