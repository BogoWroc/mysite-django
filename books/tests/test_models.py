from assertpy import assert_that
from django.test import TestCase

from books.factories import AuthorFactory
from books.models import Author


# Everything can be found at https://docs.djangoproject.com/el/1.10/ref/models/querysets/

class CrudOperationsTest(TestCase):
    def test_find_selected_author_stored_in_db(self):
        # given
        # Instance is automatically added to db
        author = AuthorFactory(first_name="bogumil")

        # when
        # Find author in db
        actual = Author.objects.get(first_name="bogumil")

        # then
        assert_that(actual).is_equal_to(author)

    def test_that_all_authors_will_be_found(self):
        # given
        authors = AuthorFactory.create_batch(20)

        # when
        # all is translated to select * from
        actual = Author.objects.all()

        # then
        assert_that(len(actual)).is_equal_to(20)

    def test_that_only_athors_with_gmail_account_will_be_found(self):
        # given
        author1 = AuthorFactory(email="author1@gmail.com")
        author2 = AuthorFactory(email="author2@wp.pl")
        author3 = AuthorFactory(email="author3@poczta.onet.pl")
        author4 = AuthorFactory(email="author4@gmail.com")

        # when
        # email__contains is translated to WHERE email LIKE '%gmail.com%';
        found_authors = Author.objects.filter(email__contains="gmail.com")

        # then
        assert_that(len(found_authors)).is_equal_to(2)
        assert_that(found_authors).contains(author1, author4)
        assert_that(found_authors).does_not_contain(author2, author3)

    def test_that_only_athors_which_has_not_got_gmail_account_will_be_found(self):
        # given
        author1 = AuthorFactory(email="author1@gmail.com")
        author2 = AuthorFactory(email="author2@wp.pl")
        author3 = AuthorFactory(email="author3@poczta.onet.pl")
        author4 = AuthorFactory(email="author4@gmail.com")

        # when
        # email__contains is translated to WHERE email NOT LIKE '%gmail.com%';
        found_authors = Author.objects.exclude(email__contains="gmail.com")

        # then
        assert_that(len(found_authors)).is_equal_to(2)
        assert_that(found_authors).contains(author2, author3)
        assert_that(found_authors).does_not_contain(author1, author4)
