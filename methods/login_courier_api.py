import requests
from data.urls import Urls
import allure

class LoginCourierApi:
    @staticmethod
    @allure.step('Вызываем метод авторизации курьера')
    def post_login_courier(login,password):
        payload = {"login":login,"password":password}
        response = requests.post(Urls.URL_LOGIN_COURIER,data=payload)
        return response