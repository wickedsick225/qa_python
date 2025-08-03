import pytest

from main import BooksCollector

class TestBooksCollector:


    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2



    @pytest.mark.parametrize('name', ['', 'a'*41])
    def test_add_new_book_invalid_name(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.books_genre


    def test_set_book_genre_success(self,collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга','Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'


    def test_set_book_genre_nonexistent_book(self,collector):
        collector.set_book_genre('Несуществующая книга','Фантастика')
        assert collector.get_book_genre('Несуществующая книга') is None


    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Фантастическая книга')
        collector.set_book_genre('Фантастическая книга', 'Фантастика')
        assert 'Фантастическая книга' in collector.get_books_with_specific_genre('Фантастика')


    def test_get_books_for_children(self, collector):
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга','Мультфильмы')
        assert 'Детская книга' in collector.get_books_for_children()


    def test_get_books_for_children(self, collector):
        collector.add_new_book('Недетская книга')
        collector.set_book_genre('Недетская книга','Ужасы')
        assert 'Недетская книга' not in collector.get_books_for_children


    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Любимая книга')
        collector.favorites.append('Любимая книга')
        assert 'Любимая книга' in collector.get_list_of_favorites_books()


    def test_add_book_in_favorites_nonexistent_book(self, collector):
        collector.faborites.append('Жеребенок')
        assert 'Жеребенок' not in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Исчезнувшая')
        collector.favorites.append('Исчезнувшая')
        collector.favorites.remove('Исчезнувшая')
        assert 'Исчезнувшая' not in collector.get_list_of_favorites_books()
