class HotBeverage:
    price = 0.30
    name = "hot beverage"

    def description(self) -> str:
        return "Just some hot water in a cup."

    def __str__(self):
        return (
            "name : "
            + self.name
            + "\n"
            + "price : "
            + f"{self.price:.2f}"
            + "\n"
            + "description : "
            + self.description()
        )


class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40

    def description(self) -> str:
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    name = "tea"


class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50

    def description(self) -> str:
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45

    def description(self) -> str:
        return "Un po' di Italia nella sua tazza!"


def main():
    beverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()
    print(beverage)
    print(coffee)
    print(tea)
    print(chocolate)
    print(cappuccino)


if __name__ == "__main__":
    main()
