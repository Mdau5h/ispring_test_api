from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class Config(BaseSettings):

    BASE_URL: str
    GITHUB_TOKEN: str
    TEST_REPO: str
    TEST_USERNAME: str


config = Config()
