from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # проверка добавления новой кинги
    def test_add_new_book(self):
        collector = BooksCollector()
        new_book ='Будни автотестировщика'
        collector.add_new_book(new_book)
        assert len(collector.get_books_genre()) == 1

    # проверка добавления двух книг
    def test_add_new_book_add_two_books(self, collector):
        # фикстура collector создаёт класс BooksCollector и добавляет 1 книгу 'Изучение Python за один день'
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

      # проверяем ГЗ, что книга названием в 40 символов, добавляется
    def test_add_new_book_when_name_than_40_characters(self):
        collector = BooksCollector()
        collector.add_new_book('Как начать писать автотесты для проверки')
        assert len(collector.get_books_genre()) == 1

    # проверяем, что книга, которая уже есть в словаре не добавляется
    def test_not_add_new_book_when_book_is_in_the_dictionary(self, collector):
        collector.add_new_book('Изучение Python за один день')
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
    def test_get_book_with_scpecific_genre(self):
        collector = BooksCollector()
        new_books_genre = {'Фантастические твари':'Фантастика',
                           'Ужас ужасный': 'Ужасы',
                           'Ужас вчерашний': 'Ужасы',
                           'Фантасты тоже плачут': 'Фантастика'}
        collector.books_genre.update(new_books_genre)
        dict_genre = collector.get_books_with_specific_genre('Фантастика')
        assert len(dict_genre) == 2
    # надо продумать негативные сценарии для списка

    # проверяем, получение словаря
    def test_get_books_genre(self, collector):
        book_name = 'Изучение Python за один день'
        book_genre = 'Ужасы'
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_books_genre() == {book_name:book_genre}

    # проверяем вывод книг подходящим детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        new_books_genre = {'Фантастические твари':'Фантастика',
                           'Ужас ужасный': 'Ужасы',
                           'Ужас вчерашний': 'Ужасы',
                           'Фантасты тоже плачут': 'Фантастика'}
        collector.books_genre.update(new_books_genre)
        children_book = collector.get_books_for_children()
        assert len(children_book) == 2
    # надо продумать негативные сценарии для списка

    # проверяем добавление книг в избранное
    def test_add_book_in_favorites(self,collector):
        book_name = 'Изучение Python за один день'
        collector.add_book_in_favorites(book_name)
        assert collector.favorites == ['Изучение Python за один день']

    # проверяем добавление нескольких книг в избранное
    def test_add_three_book_in_favorites(self):
        collector = BooksCollector()
        books = ['Изучение Python за один день', 'Тестирование для тестировщика','Как разделить слона']
        dict_books = dict.fromkeys(books, 'Фантастика')
        collector.books_genre.update(dict_books)
        for book in books:
            collector.add_book_in_favorites(book)
        assert collector.favorites == books

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
