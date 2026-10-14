from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Product:
    name: str
    price: int
    quantity: int

CATALOG: dict[str, Product] = {
    "A1": Product(name="Soda", price=3, quantity=20),
    "A2": Product(name="Chips", price=5, quantity=10),
    "A3": Product(name="Chocolate", price=4, quantity=20),
    "B1": Product(name="Juice", price=5, quantity=10),
    "B2": Product(name="Jelly beans", price=7, quantity=15),
    "B3": Product(name="zaza", price=100, quantity=2),
}

class MachineState(Enum):
    IDLE = auto()
    HAS_MONEY = auto()
    DISPENSING = auto()
    RETURNING_CHANGE = auto()

class VendingMachine():
    def __init__(self, catalog: dict[str, Product]):
        self.state = MachineState.IDLE
        self.balance = 0
        self.catalog = self.catalog

    def insert_coin(self, amount):
        if self.state in (MachineState.DISPENSING, MachineState.RETURNING_CHANGE):
            raise RuntimeError("Cannot insert coins while the machine is busy")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        self.state = MachineState.HAS_MONEY
    def choosing_product(self, code):
        if self.state != MachineState.HAS_MONEY:
            raise RuntimeError("Insert money first")
        product = self.cataloge.get(code)
        if product is None:
            raise RuntimeError(f"Unkown product code {code}")
        if product.quantity <= 0:
            raise RuntimeError("Can't you see through glass???")
        if self.balance < product.price:
            raise RuntimeError("Not enough money for this product")
        elif:
            