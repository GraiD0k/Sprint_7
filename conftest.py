import pytest
from methods.login_courier_api import LoginCourierApi
from data.helpers import Random_string
from methods.base_api import BaseApi

@pytest.fixture
def create_courier():
    login = Random_string.generate_random_string
    password = Random_string.generate_random_string
    first_name = Random_string.generate_random_string
    response_create = BaseApi.post_create_courier(login, password, first_name)
    response_login = LoginCourierApi.post_login_courier(login, password)
    created_courier_id = response_login.json()['id']
    yield login, password  # Можно добавить очистку после теста при необходимости
    if response_create.status_code == 201:
       BaseApi.delete_courier(created_courier_id)

@pytest.fixture
def courier_data():
    return {"login": Random_string.generate_random_string,"password": Random_string.generate_random_string,"first_name": Random_string.generate_random_string}
