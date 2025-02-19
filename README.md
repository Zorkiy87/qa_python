# qa_python

#по коду реализованы следующие проверки: 

    # проверка добавления новой кинги
    test_add_new_book(self):

    # проверка добавления двух книг
    test_add_new_book_add_two_books(self, collector):

      # проверяем ГЗ, что книга названием в 40 символов, добавляется
    test_add_new_book_when_name_than_40_characters(self):

    # проверяем, что книга, которая уже есть в словаре не добавляется
    test_not_add_new_book_when_book_is_in_the_dictionary(self, collector):

    # проверяем, что книга названием более 40 символов, не добавляется
    test_not_add_new_book_when_name_more_than_40_characters(self):
        
    # проверяем, что книга без названия не добавляется
    test_not_add_new_book_without_a_name(self):
       
    # проверяем, что добавляется жанр книги при наличии жанра и книги в списке
    test_set_book_genre_with_name_and_genre_on_dict(self, collector):
        
    # проверяем, что жанр не добавится, если нет жанра в списке жанров
    test_not_set_book_genre_without_a_genre_on_dict(self, collector):
       
    # проверяем, что жанр не добавится, если нет книги в списке книг жанра
    test_not_set_book_genre_without_a_name_on_dict(self,collector):
        
    # проверяем, получение жанра книги по имени
    test_get_book_genre(self, collector):
       
    # проверяем вывод списка книг по жанру
    test_get_book_with_scpecific_genre(self):
        
    # проверяем, получение словаря
    test_get_books_genre(self, collector):
        
    # проверяем вывод книг подходящим детям
    test_get_books_for_children(self):
       
    # проверяем добавление книг в избранное
    test_add_book_in_favorites(self,collector):
       
    # проверяем добавление нескольких книг в избранное
    test_add_three_book_in_favorites(self):
       
    # проверяем что дубликат книги не добавляется в избранное
    test_add_book_in_favorites(self,collector):
        
    # проверяем удаление книг из избранного
    test_delete_book_from_favorites(self,collector):
     
    # проверяем получение списка Избранных книг
    test_get_list_of_favorites_books(self,collector):
      