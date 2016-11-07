from assertpy import assert_that
from django.test import TestCase

from books.factories import AuthorFactory
from books.models import Author


class CrudOperationsTest(TestCase):
    def test_find_selected_author_stored_in_db(self):
        # given
        # Instance is automatically added to db
        author = AuthorFactory(first_name="bogumil")

        # when
        # Find author in db
        actual = Author.objects.get(first_name="bogumil")

        # then
        assert_that(author).is_equal_to(actual)
