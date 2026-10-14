from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Product:
    name: str
    price: int
    quantity: int

CATALOG: dict[str, Product] {
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
    
