
import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.saucedemo.com",
).rstrip("/")

TEST_USERNAME = os.getenv(
    "TEST_USERNAME",
    "standard_user",
)

TEST_PASSWORD = os.getenv(
    "TEST_PASSWORD",
    "secret_sauce",
)

INVENTORY_URL = f"{BASE_URL}/inventory.html"
