import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, '../../db.sqlite')}"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "bhaskarsaini333@gmail.com"
SMTP_PASSWORD = "hwlxdewbqnxsspce"
EMAIL_FROM = "bhaskarsaini333@gmail.com"
EMAIL_TO = "prajwalbandi14@gmail.com"

BATCH_SIZE = 10
