import pytest
from order import Order, OrderRepository, EmailService


def test_order_total():
    items = [{"name": "Pizza", "price": 10}, {"name": "Cola", "price": 5}]
    order = Order(items)
    assert order.calculate_total() == 15


def test_order_repository_saves_order(capsys):
    items = [{"name": "Burger", "price": 8}]
    order = Order(items)
    repo = OrderRepository()
    repo.save(order)
    captured = capsys.readouterr()
    assert "Saving order with total 8" in captured.out


def test_email_service_sends_confirmation(capsys):
    items = [{"name": "Salad", "price": 6}]
    order = Order(items)
    email = EmailService()
    email.send_order_confirmation(order)
    captured = capsys.readouterr()
    assert "Email sent for order total: 6" in captured.out
