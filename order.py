class Order:
    def __init__(self, items: list[dict]):
        """
        items: list of dicts, e.g. [{"name": "Pizza", "price": 12}]
        """
        self.items = items

    def calculate_total(self) -> float:
        """Calculate the total price of all items."""
        return sum(item["price"] for item in self.items)


class OrderRepository:
    def save(self, order: Order) -> None:
        """Simulate saving order to a database."""
        print(f"💾 Saving order with total {order.calculate_total()} to database...")


class EmailService:
    def send_order_confirmation(self, order: Order) -> None:
        """Simulate sending an email confirmation for the order."""
        print(f"📧 Email sent for order total: {order.calculate_total()}")


if __name__ == "__main__":
    # Example usage
    items = [{"name": "Pizza", "price": 12}, {"name": "Cola", "price": 3}]
    order = Order(items)

    repo = OrderRepository()
    repo.save(order)

    email = EmailService()
    email.send_order_confirmation(order)
