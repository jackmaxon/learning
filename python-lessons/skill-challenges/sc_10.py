from dataclasses import dataclass

@dataclass(frozen=True)
class Stock:
    ticker: str
    price: int | float
    dividend: int | float = 0
    dividend_frequency: int = 4

    @property
    def annual_dividend(self):
        return self.dividend * self.dividend_frequency

@dataclass(order = True)
class Position:
    stock: Stock
    shares: int | float

    def __post_init__(self):
        if not isinstance(self.stock, Stock):
            raise ValueError("'stock' must be an instance of the Stock dataclass.")
        
        if not self.shares > 0:
            raise ValueError("'shares' must be positive.")

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.stock.price * self.shares == other.stock.price * other.shares
    
    def __gt__(self, other):
        if not isinstance(other, Position):
            return False
        return self.stock.price * self.shares > other.stock.price * other.shares

@dataclass
class Portfolio:
    holdings: list[Position]

    @property
    def value(self):
        return sum(pos.shares * pos.stock.price for pos in self.holdings) 

    @property
    def portfolio_yield(self):
        return sum(pos.stock.annual_dividend for pos in self.holdings) / self.value