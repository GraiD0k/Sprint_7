import allure
import pytest
from methods.create_orders_api import CreateOrdersApi
from data.create_orders_data import CreateOrdersData

class TestCreateOrders:
    @pytest.mark.parametrize("order_date", [
        (
                {'first_name': 'Тестировщик', 'last_name': 'Автоматизаторов', 'address': 'Konoha, 142 apt.',
                 'metro_station': 4,'phone':'+7 800 555 35 35','rent_time':100,'delivery_date':'2000-01-01',
                 'comment':'ПРИВЕЗИТЕ СКОРЕЕ мой товар','color': 'BLACK'}
        ),
        (
                {'first_name': 'Автоматизатор', 'last_name': 'Тестеров', 'address': 'Тест, Московская, д96, кв 666',
                 'metro_station': 12,'phone':'8 800 666 36 36','rent_time':69,'delivery_date':'2025-10-10',
                 'comment':'Не разбейте ничего','color': 'GREY'}
        ),
        (
                {'first_name': 'Тест', 'last_name': 'Лидов', 'address': 'Питер, Соляная, д6, кв 666/2',
                 'metro_station': 1, 'phone': '8 800 777 30 36', 'rent_time': 96, 'delivery_date': '2024-10-10',
                 'comment': 'Просто по красота', 'color': "'BLACK','GREY'"}
        ),
        (
                {'first_name': 'Тест', 'last_name': 'Лидов', 'address': 'Питер, Соляная, д6, кв 666/2',
                 'metro_station': 1, 'phone': '8 800 777 30 36', 'rent_time': 96, 'delivery_date': '2024-10-10',
                 'comment': 'Просто по красота', 'color': ''}
        )
    ])
    @allure.title('Создание заказа')
    def test_create_orders(self, order_date):
        response_create = CreateOrdersApi.post_login_courier(order_date['first_name'],
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