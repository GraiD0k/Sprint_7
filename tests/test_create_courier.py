import allure
from methods.base_api import BaseApi
from data.create_login_data import CreateLoginData




class TestCreateCourier:

    @allure.title('Создание курьера')
    def test_create_courier(self,generate_random_string):
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string
        response = BaseApi.post_create_courier(login,password,first_name)
        with allure.step('Проверяем код и текст ответа'):
            assert response.status_code==201 and response.text == CreateLoginData.TEXT_CREATE_COURIER_201

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_courier_create_two_courier_error(self,generate_random_string):
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string
        response = BaseApi.post_create_courier(login,password,first_name)
        response_error = BaseApi.post_create_courier(login, password, first_name)
        with allure.step('Проверяем код и текст ответа'):
            assert response_error.status_code==409 and response_error.text == CreateLoginData.TEXT_CREATE_COURIER_409

    @allure.title('Создание курьера - не заполнен логин')
    def test_create_courier_no_login_error(self,generate_random_string):
        login = ''
        password = generate_random_string
        first_name = generate_random_string
        response = BaseApi.post_create_courier(login, password, first_name)
        with allure.step('Проверяем код и текст ответа'):
            assert response.status_code == 400 and response.text == CreateLoginData.TEXT_CREATE_COURIER_400

    @allure.title('Создание курьера - не заполнен пароль')
    def test_create_courier_no_password_error(self, generate_random_string):
        login = generate_random_string
        password = ''
        first_name = generate_random_string
        response = BaseApi.post_create_courier(login, password, first_name)
        with allure.step('Проверяем код и текст ответа'):
            assert response.status_code == 400 and response.text == CreateLoginData.TEXT_CREATE_COURIER_400