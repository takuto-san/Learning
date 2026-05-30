## Logging

ディレクトリ構成
```
my_paypay_app/
├── logger_config.py # ロガーの設定
├── payment.py # 決済機能を定義
└── main.py # 実行部分
```

### if __name__ == '__main__'について
```
Pythonには特別な変数 __name__ があり、
ファイルを直接実行したとき ➔ __name__ == '__main__'
他のファイルからインポートされたとき ➔ __name__ == 'ファイル名（モジュール名）'
になるというルールがある。

つまり、__name__ == '__main__' をつけないとimportされたときに関数が実行されてしまう。
ファイルを直接実行したときだけファイル内の処理を実行するようにしたのが、__name__ == '__main__'
```

logger_config.py
```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger:
    """
    name: ロガー名
    log_file: ログ出力ファイル名
    level: ログレベル
    """
    # payment.logファイルの出力を定義。
    formatter = logging.Formatter(
        # %記法: 変数を文字列として代入
        fmt="%(asctime)s - %(levelname)-8s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # ファイルハンドラを作成
    file_handler = RotatingFileHandler(
        log_file, maxBytes=1_000_000, backupCount=3, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # コンソール出力用のハンドラを作成
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # loggerインスタンスには、.info(), .warning()などログ出力のメソッドがある。
    logger = logging.getLogger(name) # payment
    logger.setLevel(level)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger


```

payment.py
```python
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
```

main.py
```python
from payment import Payment, PaymentError

def main():
    wallet = Payment(1000)
    try:
        wallet.charge(500)
        wallet.pay(200)
        wallet.pay(2000)  # This should raise an error
    except PaymentError as e:
        print(f"Charge failed: {e}")

if __name__ == "__main__":
    main()
```



実行
```console
$ cd Logging 
$ python main.py
```

出力（payment.logファイル）
```
2025-04-28 17:22:48 - INFO     - payment - Initialized Payment with balance=1000.00
2025-04-28 17:22:48 - INFO     - payment - Charged successful: +500.00, new balance=1500.00
2025-04-28 17:22:48 - INFO     - payment - Paid successful: -200.00, new balance=1300.00
2025-04-28 17:22:48 - WARNING  - payment - Payment declined: insufficient balance (requested=2000.00, balance=1300.00)
```