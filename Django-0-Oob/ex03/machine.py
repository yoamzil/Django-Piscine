import random

from beverages import HotBeverage, Coffee, Tea, Cappuccino


class CoffeMachine:
    def __init__(self):
        self.drinkServed = 0
        self.is_broken = False

    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90

        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.drinkServed = 0
        self.is_broken = False

    def serve(self, beverage_class):
        if self.is_broken:
            raise self.BrokenMachineException()

        self.drinkServed += 1
        if self.drinkServed == 10:
            self.is_broken = True
        if random.randint(0, 1) == 0:
            return beverage_class()
        else:
            return self.EmptyCup()


def main():
    cm = CoffeMachine()
    try:
        while True:
            coffee = cm.serve(Coffee)
            print(coffee)
            tea = cm.serve(Tea)
            print(tea)
            cappuccino = cm.serve(Cappuccino)
            print(cappuccino)            
    except CoffeMachine.BrokenMachineException as e:
        print(e)
    cm.repair()
    try:
        while True:
            coffee = cm.serve(Coffee)
            print(coffee)
            tea = cm.serve(Tea)
            print(tea)
            cappuccino = cm.serve(Cappuccino)
            print(cappuccino)            
    except CoffeMachine.BrokenMachineException as e:
        print(e)


if __name__ == "__main__":
    main()
