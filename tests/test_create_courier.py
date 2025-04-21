import allure
from methods.base_api import BaseApi
from data.create_login_data import CreateLoginData
import pytest
from helpers.helpers import Random_string



class TestCreateCourier:


    @allure.title('Создание курьера')
    def test_create_courier(self,courier_data):
        response = BaseApi.post_create_courier(courier_data['login'], courier_data['password'], courier_data['first_name'])
        with allure.step('Проверяем код и текст ответа'):
            assert response.status_code==201 and response.text == CreateLoginData.TEXT_CREATE_COURIER_201

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_courier_create_two_courier_error(self,courier_data):
        response = BaseApi.post_create_courier(courier_data['login'], courier_data['password'], courier_data['first_name'])
        response_error = BaseApi.post_create_courier(courier_data['login'], courier_data['password'], courier_data['first_name'])
        with allure.step('Проверяем код и текст ответа'):
            assert response_error.status_code==409 and response_error.text == CreateLoginData.TEXT_CREATE_COURIER_409

    @pytest.mark.parametrize(
        "missing_field, expected_error",
        [("login", CreateLoginData.TEXT_CREATE_COURIER_400),
         ("password", CreateLoginData.TEXT_CREATE_COURIER_400),
        ],
        ids=["missing_login", "missing_password"]
    )
    @allure.title("Создание курьера - не заполнен {missing_field}")
    def test_create_courier_missing_fields(self,missing_field,expected_error):
        login = Random_string.generate_random_string if missing_field != "login" else ""
        password = Random_string.generate_random_string if missing_field != "password" else ""
        first_name = Random_string.generate_random_string

        response = BaseApi.post_create_courier(login, password, first_name)

        with allure.step('Проверяем код и текст ответа'):
            assert response.status_code == 400
            assert response.text == expected_error