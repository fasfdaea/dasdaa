class Product:
    """Товар с ценой и количеством на складе."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self) -> None:
        """Показать информацию о товаре."""
        print(
            f"Товар: {self.name} | Цена: {self.price:.2f} | "
            f"На складе: {self.quantity} шт."
        )

    def buy(self, amount: int) -> bool:
        """Купить указанное количество, если его хватает на складе."""
        if amount <= 0:
            raise ValueError("Количество для покупки должно быть положительным")

        if amount > self.quantity:
            print(
                f"Недостаточно товара «{self.name}»: "
                f"доступно {self.quantity}, запрошено {amount}. Покупка не выполнена."
            )
            return False

        self.quantity -= amount
        print(f"Куплено {amount} шт. товара «{self.name}».")
        return True

    def replenish(self, amount: int) -> None:
        """Добавить указанное количество товара на склад."""
        if amount <= 0:
            raise ValueError("Количество для пополнения должно быть положительным")

        self.quantity += amount
        print(f"Склад пополнен на {amount} шт. товара «{self.name}».")



products = [
    Product("Книга", 750.00, 12),
    Product("Настольная лампа", 2490.00, 5),
    Product("Кружка", 390.00, 20),
]

if __name__ == "__main__":
    for product in products:
        product.show_info()

    products[0].buy(2)
    products[1].buy(10) 
    products[2].replenish(5)

    print("\nСостояние склада после операций:")
    for product in products:
        product.show_info()
