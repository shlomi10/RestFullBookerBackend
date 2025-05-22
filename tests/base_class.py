import os

from dotenv import load_dotenv

dot_env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils", ".env"))
load_dotenv(dotenv_path=dot_env_path)

class BaseClass:
    def __init__(self, page):
        self.page = page
        self.base_url = os.getenv("BASE_URL")
        self.admin = os.getenv("ADMIN_USER")
        self.pwd = os.getenv("ADMIN_PW")