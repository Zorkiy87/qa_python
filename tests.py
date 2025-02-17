from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверяем ГЗ, что книга названием в 40 символов, добавляется
    def test_add_new_book_when_name_than_40_characters(self):
        collector = BooksCollector()
        collector.add_new_book('Как начать писать автотесты для проверки')
        assert len(collector.get_books_genre()) == 1


    # проверяем, что книга, которая уже есть в словаре не добавляется
    def test_not_add_new_book_when_book_is_in_the_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    # проверяем, что книга названием более 40 символов, не добавляется
    def test_not_add_new_book_when_name_more_than_40_characters(self):
        collector = BooksCollector()
        collector.add_new_book('Как начать писать автотесты для проверки?')
        assert len(collector.get_books_genre()) == 0


    # проверяем, что книга без названия не добавляется
    def test_not_add_new_book_without_a_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    # проверяем, что добавляется жанр книги при наличии жанра и книги в списке
    def test_set_book_genre_with_name_and_genre_on_dict(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name,'Ужасы')
        # print(collector.books_genre.get('Гордость и предубеждение и зомби'))
        assert collector.books_genre.get(book_name) == 'Ужасы'

    # проверяем, что жанр не добавится, если нет жанра в списке жанров
    def test_not_set_book_genre_without_a_genre_on_dict(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Популярное')
        assert collector.books_genre.get(book_name) == ''

    # проверяем, что жанр не добавится, если нет книги в списке книг жанра
    def test_not_set_book_genre_without_a_name_on_dict(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.set_book_genre('Гордость и зомби', 'Ужасы')
        assert collector.books_genre.get(book_name) == ''

    # проверяем, получение жанра книги по имени
    def test_get_book_genre(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)


        # print(collector.books_genre)