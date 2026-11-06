def format_coins(amount: float) -> str:
    return f"{amount:,.2f}".replace(",", " ").replace(".", ",") + " монет"


class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self) -> None:
        print(f"{self.name} — {format_coins(self.price)}, на складе: {self.quantity} шт.")

    def buy(self, amount: int) -> bool:
        if amount <= 0:
            raise ValueError("Количество для покупки должно быть положительным")

        if amount > self.quantity:
            print(
                f"Не удалось купить товар «{self.name}»: "
                f"на складе {self.quantity} шт., а запрошено {amount} шт."
            )
            return False

        self.quantity -= amount
        print(f"Покупка выполнена: {amount} шт. — {self.name}.")
        return True

    def replenish(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Количество для пополнения должно быть положительным")

        self.quantity += amount
        print(f"На склад добавлено {amount} шт. товара «{self.name}».")


products = [
    Product("Книга", 750.00, 12),
    Product("Настольная лампа", 2490.00, 5),
    Product("Кружка", 390.00, 20),
]


def show_products(title: str = "Каталог товаров") -> None:
    print(f"\n{title}:")
    for number, product in enumerate(products, start=1):
        print(f"{number}. ", end="")
        product.show_info()


def choose_product(action: str):
    print(f"\nВыберите товар, который хотите {action}:")
    for number, product in enumerate(products, start=1):
        print(
            f"{number}. {product.name} — {format_coins(product.price)}, "
            f"остаток: {product.quantity} шт."
        )

    try:
        number = int(input(f"Введите номер товара от 1 до {len(products)}: "))
    except ValueError:
        print("Введите номер товара целым числом.")
        return None

    if number < 1 or number > len(products):
        print("Товара с таким номером нет.")
        return None

    product = products[number - 1]
    print(f"Выбран товар: {product.name}.")
    return product


def read_amount(prompt: str):
    try:
        amount = int(input(prompt))
    except ValueError:
        print("Введите количество целым числом.")
        return None

    if amount <= 0:
        print("Количество должно быть больше нуля.")
        return None

    return amount


def run_shop() -> None:
    while True:
        print("\n=== Магазин ===")
        print("1. Просмотреть каталог")
        print("2. Купить товар")
        print("3. Добавить поставку на склад")
        print("0. Выйти")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_products("Каталог и остатки")
        elif choice == "2":
            product = choose_product("купить")
            if product is None:
                continue

            amount = read_amount(
                f"Сколько штук купить? Сейчас на складе: {product.quantity}. "
            )
            if amount is None:
                continue

            if amount > product.quantity:
                product.buy(amount)
                continue

            total_price = product.price * amount
            print(f"\nВы выбрали: {product.name}")
            print(f"Количество: {amount} шт.")
            print(f"Сумма к оплате: {format_coins(total_price)}")
            confirmation = input("Подтвердить покупку? (д/н): ").strip().lower()
            if confirmation in ("д", "да"):
                if product.buy(amount):
                    print(f"Остаток на складе: {product.quantity} шт.")
            else:
                print("Покупка отменена. Остаток не изменён.")
        elif choice == "3":
            product = choose_product("принять на склад")
            if product is None:
                continue

            amount = read_amount(
                f"Сколько штук товара «{product.name}» поступило? "
            )
            if amount is not None:
                previous_quantity = product.quantity
                product.replenish(amount)
                print(
                    f"Остаток изменился: {previous_quantity} -> "
                    f"{product.quantity} шт."
                )
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Такого пункта нет. Выберите действие из меню.")


if __name__ == "__main__":
    run_shop()
