import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.add_new_book('Изучение Python за один день')
    return collector