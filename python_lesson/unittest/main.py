class PaymentError(Exception):
    """Base class for payment-related exceptions."""
    pass

class payment:
    def __init__(self,initial_balance: float = 0):
        self.balance = initial_balance

    def charge(self, amount: float):
        if amount <= 0:
            raise PaymentError("Charge amount must be positive.")
        self.balance += amount
        return self.balance
    
    def pay(self, amount: float):
        if amount <= 0:
            raise PaymentError("Payment amount must be positive.")
        if amount > self.balance:
            raise PaymentError("Insufficient balance.")
        self.balance -= amount
        return self.balance