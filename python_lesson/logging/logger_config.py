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
