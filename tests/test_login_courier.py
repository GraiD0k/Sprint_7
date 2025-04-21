import allure
from methods.login_courier_api import LoginCourierApi
from data.login_courier_data import LoginCourierData


class TestLoginCourier:
    @allure.title('Авторизация')
    def test_login_courier(self, create_courier):
        login, password = create_courier
        response_login = LoginCourierApi.post_login_courier(login, password)
        with allure.step('Проверяем код и текст ответа'):
            assert response_login.status_code == 200 and LoginCourierData.TEXT_LOGIN_COURIER_200 in response_login.text



    @allure.title('Авторизация - не передан логин')
    def test_login_courier_no_login_error(self, create_courier):
        password = create_courier
        response_login = LoginCourierApi.post_login_courier('',password)
        with allure.step('Проверяем код и текст ответа'):
            assert response_login.status_code == 400 and response_login.text == LoginCourierData.TEXT_LOGIN_COURIER_400

    @allure.title('Авторизация - не передан пароль')
    def test_login_courier_no_password_error(self, create_courier):
        login = create_courier
        response_login = LoginCourierApi.post_login_courier(login,'')
        with allure.step('Проверяем код и текст ответа'):
            assert response_login.status_code == 400 and response_login.text == LoginCourierData.TEXT_LOGIN_COURIER_400

    @allure.title('Авторизация под несуществующим пользователем, запрос возвращает ошибку')
    def test_login_courier_no_exist_courier_error(self):
        response_login = LoginCourierApi.post_login_courier('Alekseev_test','123')
        with allure.step('Проверяем код и текст ответа'):
            assert response_login.status_code == 404 and response_login.text == LoginCourierData.TEXT_LOGIN_COURIER_404

    @allure.title('Авторизация - неправильно указать пароль')
    def test_login_courier_wrong_password_error(self,create_courier):
        login = create_courier
        response_login = LoginCourierApi.post_login_courier(login,'123')
        with allure.step('Проверяем код и текст ответа'):
            assert response_login.status_code == 404 and response_login.text == LoginCourierData.TEXT_LOGIN_COURIER_404