from logger_config import setup_logger

class PaymentError(Exception):
    """Custom exception for payment errors."""
    pass

# 継承しカスタマイズすることで柔軟にログ出力を定義できる。
logger = setup_logger("payment", "payment.log")

class Payment:
    def __init__(self, initial_balance: float = 0):
        self.balance = initial_balance
        # logging.infoは、ターミナル版のprint文みたいなもの。ただし、出力するかどうかはログレベル次第。
        logger.info("Initialized Payment with balance=%.2f", self.balance)

    def charge(self, amount: float):
        if amount <= 0:
            logger.error("Charge failed: amount must be positive (got %.2f)", amount)
            raise PaymentError("Charge amount must be positive.")
        self.balance += amount
        logger.info("Charged successful: +%.2f, new balance=%.2f", amount, self.balance)
        return self.balance

    def pay(self, amount: float) -> float:
        logger.debug("Attempting to pay amount: %.2f", amount)
        if amount <= 0:
            logger.error("Payment failed: amount must be positive (got %.2f)", amount)
            raise PaymentError("Payment amount must be positive.")
        if amount > self.balance:
            logger.warning(
                "Payment declined: insufficient balance (requested=%.2f, balance=%.2f)",
                amount, self.balance
            )
            raise PaymentError("Insufficient balance.")
        self.balance -= amount
        logger.info("Paid successful: -%.2f, new balance=%.2f", amount, self.balance)
        return self.balance