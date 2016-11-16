from assertpy import assert_that
from django.test import TestCase

from books.factories import AuthorFactory, BookFactory
from books.models import Author, Book


# Everything can be found at https://docs.djangoproject.com/el/1.10/ref/models/querysets/

class CrudOperationsTest(TestCase):
    def setUp(self):
        self.author1 = AuthorFactory(first_name="Author1", email="author1@gmail.com")
        self.author2 = AuthorFactory(first_name="Author2", email="author2@wp.pl")
        self.author3 = AuthorFactory(first_name="Author3", email="author3@poczta.onet.pl")
        self.author4 = AuthorFactory(first_name="Author4", email="author4@gmail.com")
        self.book1 = BookFactory(authors=[self.author1])
        self.book2 = BookFactory(title="World 1", authors=[self.author1])
        self.book3 = BookFactory(title="Next world 2", authors=[self.author1])

    def tearDown(self):
        Author.objects.all().delete()
        Book.objects.all().delete()

    def test_find_selected_author_stored_in_db(self):
        # when
        # Find author in db
        actual = Author.objects.get(first_name="Author1")

        # then
        assert_that(actual).is_equal_to(self.author1)

    def test_that_all_authors_will_be_found(self):
        # given
        batch_of_additional_authors = AuthorFactory.create_batch(20)

        # when
        # all is translated to select * from
        actual = Author.objects.all()

        # then
        assert_that(len(actual)).is_equal_to(len(batch_of_additional_authors) + 4)

    def test_that_only_athors_with_gmail_account_will_be_found(self):
        # when
        # email__contains is translated to WHERE email LIKE '%gmail.com%';
        found_authors = Author.objects.filter(email__contains="gmail.com")

        # then
        assert_that(len(found_authors)).is_equal_to(2)
        assert_that(found_authors).contains(self.author1, self.author4)
        assert_that(found_authors).does_not_contain(self.author2, self.author3)

    def test_that_only_athors_which_has_not_got_gmail_account_will_be_found(self):
        # when
        # email__contains is translated to WHERE email NOT LIKE '%gmail.com%';
        found_authors = Author.objects.exclude(email__contains="gmail.com")

        # then
        assert_that(len(found_authors)).is_equal_to(2)
        assert_that(found_authors).contains(self.author2, self.author3)
        assert_that(found_authors).does_not_contain(self.author1, self.author4)

    def test_that_all_records_were_dropped(self):
        # when
        Author.objects.all().delete()
        found_authors = Author.objects.all()

        # then
        assert_that(len(found_authors)).is_equal_to(0)

    def test_that_first_author_has_a_book(self):
        # when
        author = Author.objects.get(id=1)
        book = author.book_set.get(id=1)

        # then
        assert_that(book).is_equal_to(self.book1)

    def test_that_library_contains_slected_numbers_of_books_with_title_contains_the_same_word(self):
        # when
        count = Book.objects.title_count("world")
        # then
        assert_that(count).is_equal_to(2)
