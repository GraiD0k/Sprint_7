import allure
import pytest
from methods.create_orders_api import CreateOrdersApi
from data.create_orders_data import CreateOrdersData

class TestCreateOrders:
    @pytest.mark.parametrize("order_date", [
        (
                CreateOrdersData.FIRST_ORDER
        ),
        (
                CreateOrdersData.SECOND_ORDER
        ),
        (
                CreateOrdersData.THIRD_ORDER
        ),
        (
                CreateOrdersData.FOURTH_ORDER
        )
    ])
    @allure.title('Создание заказа')
    def test_create_orders(self, order_date):
        response_create = CreateOrdersApi.post_create_order(order_date['first_name'],
                                                             order_date['last_name'],
                                                             order_date['address'],
                                                             order_date['metro_station'],
                                                             order_date['phone'],
                                                             order_date['rent_time'],
                                                             order_date['delivery_date'],
                                                             order_date['comment'],
                                                             order_date['color'],)
        with allure.step('Проверяем код и текст ответа'):
            assert response_create.status_code == 201 and CreateOrdersData.TEXT_CREATE_ORDERS_200 in response_create.text