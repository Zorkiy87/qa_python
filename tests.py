import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

      # проверяем ГЗ, что книги с ГЗ (1, 2, 39, 40 символов) в названии добавляются
    @pytest.mark.parametrize('book_name', ['К','К2','Параметризация упрощает написание теста','Параметризация упрощает написание теста!'])
    def test_add_new_book_when_name_1_2_39_40_characters(self, book_name,only_collector):
        only_collector.add_new_book(book_name)
        assert len(only_collector.get_books_genre()) == 1

      # проверяем ГЗ, что книга названием в 40 символов, добавляется
    def test_add_new_book_when_name_than_40_characters(self,only_collector):
        only_collector.add_new_book('Как начать писать автотесты для проверки')
        assert len(only_collector.get_books_genre()) == 1

    # проверяем, что книга, которая уже есть в словаре не добавляется
    def test_not_add_new_book_when_book_is_in_the_dictionary(self, collector):
        collector.add_new_book('Изучение Python за один день')
        assert len(collector.get_books_genre()) == 1

    # проверяем, что книга названием более 40 символов, не добавляется
    def test_not_add_new_book_when_name_more_than_40_characters(self,only_collector):
        only_collector.add_new_book('Как начать писать автотесты для проверки?')
        assert only_collector.get_books_genre() == {}

    # проверяем, что книга без названия не добавляется
    def test_not_add_new_book_without_a_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert collector.get_books_genre() == {}

    # проверяем, что добавляется жанр книги при наличии жанра и книги в списке
    def test_set_book_genre_with_name_and_genre_on_dict(self, collector):
        book_name = 'Изучение Python за один день'
        collector.set_book_genre(book_name,'Ужасы')
        assert collector.books_genre.get(book_name) == 'Ужасы'

    # проверяем, что жанр не добавится, если нет жанра в списке жанров
    def test_not_set_book_genre_without_a_genre_on_dict(self, collector):
        book_name = 'Изучение Python за один день'
        collector.set_book_genre(book_name, 'Популярное')
        assert collector.books_genre.get(book_name) == ''

    # проверяем, что жанр не добавится, если нет книги в списке книг жанра
    def test_not_set_book_genre_without_a_name_on_dict(self,collector):
        book_name = 'Изучение Python за один день'
        collector.set_book_genre('Гордость и зомби', 'Ужасы')
        assert collector.books_genre.get(book_name) == ''

    # проверяем, получение жанра книги по имени
    def test_get_book_genre(self, collector):
        book_name = 'Изучение Python за один день'
        collector.set_book_genre(book_name, 'Ужасы')
        assert collector.get_book_genre(book_name) == 'Ужасы'

    # проверяем вывод списка книг по жанру
    def test_get_book_with_scpecific_genre(self,only_collector):
        new_books_genre = {'Фантастические твари':'Фантастика',
                           'Ужас ужасный': 'Ужасы',
                           'Ужас вчерашний': 'Ужасы',
                           'Фантасты тоже плачут': 'Фантастика'}
        only_collector.books_genre.update(new_books_genre)
        dict_genre = only_collector.get_books_with_specific_genre('Фантастика')
        assert dict_genre == ['Фантастические твари','Фантасты тоже плачут']
        # надо продумать негативные сценарии для списка

    # проверяем, получение словаря
    def test_get_books_genre(self, collector):
        book_name = 'Изучение Python за один день'
        book_genre = 'Ужасы'
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_books_genre() == {book_name:book_genre}

    # проверяем вывод книг подходящим детям
    def test_get_books_for_children(self,only_collector):
        new_books_genre = {'Фантастические твари':'Фантастика',
                           'Ужас ужасный': 'Ужасы',
                           'Ужас вчерашний': 'Ужасы',
                           'Фантасты тоже плачут': 'Фантастика'}
        only_collector.books_genre.update(new_books_genre)
        children_book = only_collector.get_books_for_children()
        assert children_book == ['Фантастические твари','Фантасты тоже плачут']
    # надо продумать негативные сценарии для списка

    # проверяем добавление книг в избранное
    def test_add_book_in_favorites(self,collector):
        book_name = 'Изучение Python за один день'
        collector.add_book_in_favorites(book_name)
        assert collector.favorites == ['Изучение Python за один день']

    # проверяем добавление нескольких книг в избранное
    def test_add_three_book_in_favorites(self,only_collector):
        books = ['Изучение Python за один день', 'Тестирование для тестировщика','Как разделить слона']
        dict_books = dict.fromkeys(books, 'Фантастика')
        only_collector.books_genre.update(dict_books)
        for book in books:
            only_collector.add_book_in_favorites(book)
        assert only_collector.favorites == books

    # проверяем что дубликат книги не добавляется в избранное
    def test_add_book_in_favorites(self,collector):
        book_name = 'Изучение Python за один день'
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.favorites == ['Изучение Python за один день']

    # проверяем удаление книг из избранного
    def test_delete_book_from_favorites(self,collector):
        book_name = 'Изучение Python за один день'
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert collector.favorites == []

    # проверяем получение списка Избранных книг
    def test_get_list_of_favorites_books(self,collector):
        book_name = 'Изучение Python за один день'
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == ['Изучение Python за один день']
