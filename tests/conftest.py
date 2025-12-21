import pytest
from praktikum.database import Database


@pytest.fixture
def database():
    return Database()
