import logging

# 1. Pipeline için özel bir logger oluşturuyoruz
logger = logging.getLogger("ETL")
logger.setLevel(logging.INFO)

# 2. Mesajın formatı: [Zaman] [Seviye]: Mesaj
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# 3. Terminale basan Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# 4. etl.log dosyasına yazan Handler
file_handler = logging.FileHandler("etl.log", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
