import allure
from methods.get_orders_api import GetOrdersApi
from data.get_order_data import GetOrdersData

class TestGetOrders:
    @allure.title('Проверяем, что в тело ответа возвращается список заказов.')
    def test_get_orders(self):
        response_orders = GetOrdersApi.get_orders()
        with allure.step('Проверяем код и текст ответа'):
            assert response_orders.status_code == 200 and GetOrdersData.TEXT_GET_ORDERS_200 in response_orders.text