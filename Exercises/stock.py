import dataclasses


@dataclasses.dataclass
class Stock:
    name: str
    shares: int
    price: float

    def cost(self):
        return self.shares * self.price
