import pytest

from main import BooksCollector


class TestBooksCollector:
    @pytest.mark.parametrize('name, genre', [
        ['Что делать, если ваш кот хочет вас убить', 'Фантастика'],
        ['Гордость и предубеждение и зомби', 'Ужасы'],
        ['Леди и бродяга', 'Мультфильмы']
    ])
    def test_set_book_genre_positive(self, name, genre):
        set_genre = BooksCollector()
        set_genre.add_new_book(name)
        set_genre.set_book_genre(name, genre)
        assert set_genre.books_genre[name] == genre

    @pytest.mark.parametrize('name, genre', [
        ['Python для чайников', 'Научпоп'],
        ['Хоббит, или Туда и обратно', 'Фэнтези']
    ])
    def test_set_book_genre_negative(self, name, genre):
        set_genre = BooksCollector()
        set_genre.add_new_book(name)
        set_genre.set_book_genre(name, genre)
        assert set_genre.books_genre[name] == ''

    @pytest.mark.parametrize('name, genre', [
        ['Что делать, если ваш кот хочет вас убить', 'Фантастика'],
        ['Гордость и предубеждение и зомби', 'Ужасы'],
        ['Леди и бродяга', 'Мультфильмы']
    ])
    def test_get_book_genre_positive(self, name, genre):
        get_genre = BooksCollector()
        get_genre.add_new_book(name)
        get_genre.set_book_genre(name, genre)
        assert get_genre.get_book_genre(name) == genre

    def test_get_book_genre_negative(self):
        get_genre = BooksCollector()
        assert get_genre.get_book_genre('Шантарам') is None

    @pytest.mark.parametrize('name, genre', [
        ['Что делать, если ваш кот хочет вас убить', 'Фантастика'],
        ['Гордость и предубеждение и зомби', 'Ужасы'],
        ['Леди и бродяга', 'Мультфильмы']
    ])
    def test_get_books_with_specific_genre(self, name, genre):
        specific_genre = BooksCollector()
        specific_genre.add_new_book(name)
        specific_genre.set_book_genre(name, genre)
        books_with_specific_genre = specific_genre.get_books_with_specific_genre(genre)
        assert name in books_with_specific_genre

    @pytest.mark.parametrize('name, genre', [
        ['Что делать, если ваш кот хочет вас убить', 'Фантастика'],
        ['Гордость и предубеждение и зомби', 'Ужасы'],
        ['Леди и бродяга', 'Мультфильмы']
    ])
    def test_get_books_genre_positive(self, name, genre):
        get_genre = BooksCollector()
        get_genre.add_new_book(name)
        get_genre.set_book_genre(name, genre)
        actual_books_genre = get_genre.get_books_genre()
        expected_books_genre = {name: genre}
        assert actual_books_genre == expected_books_genre

    def test_get_books_for_children_positive(self):
        collection_for_children = BooksCollector()
        collection_for_children.add_new_book('Леди и бродяга')
        collection_for_children.set_book_genre('Леди и бродяга', 'Мультфильмы')
        books_for_children = collection_for_children.get_books_for_children()
        assert 'Леди и бродяга' in books_for_children

    @pytest.mark.parametrize('name, genre', [
        ['Что делать, если ваш кот хочет вас убить', 'Фантастика'],
        ['Гордость и предубеждение и зомби', 'Ужасы'],
        ['Леди и бродяга', 'Мультфильмы']
    ])
    def test_add_book_in_favorites(self, name, genre):
        favorite_collection = BooksCollector()
        favorite_collection.add_new_book(name)
        favorite_collection.set_book_genre(name, genre)
        favorite_collection.add_book_in_favorites(name)
        assert name in favorite_collection.favorites

    @pytest.mark.parametrize('name', [
        'Что делать, если ваш кот хочет вас убить',
        'Гордость и предубеждение и зомби',
        'Леди и бродяга'
    ])
    def test_delete_book_from_favorites(self, name):
        delete_favorite_book = BooksCollector()
        delete_favorite_book.add_new_book(name)
        delete_favorite_book.add_book_in_favorites(name)
        delete_favorite_book.delete_book_from_favorites(name)
        assert name not in delete_favorite_book.favorites

    def test_get_list_of_favorites_books(self):
        favorite_books = BooksCollector()
        favorite_books.add_new_book('Леди и бродяга')
        favorite_books.add_book_in_favorites('Леди и бродяга')
        favorites = favorite_books.get_list_of_favorites_books()
        assert 'Леди и бродяга' in favorites

    @pytest.mark.parametrize('book_name, expected', [
        ('Книга с очень длинным названием которое превышает лимит в 40 символов', False),
        ('Нормальная книга', True),
        ('', False),  
        ('К', True),  
        ('К' * 40, True),  
        ('К' * 41, False),  
    ])
    def test_add_new_book_name_length_validation(self, collector, book_name, expected):
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected
