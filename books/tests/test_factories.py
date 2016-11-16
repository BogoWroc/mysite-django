from assertpy import assert_that
from django.test import TestCase

from books.factories import PublisherFactory, AuthorFactory, BookFactory, PersonFactory
from books.models import Publisher, Book, Person


class InstanceCreationTest(TestCase):
    def test_that_publisher_can_be_created(self):
        # given
        publisher = PublisherFactory()

        # when
        actual = Publisher.objects.get(name=publisher.name)

        # then
        assert_that(actual).is_equal_to(publisher)

    def test_that_book_can_be_created(self):
        # given
        author = AuthorFactory()
        book = BookFactory(authors=[author], )

        # when
        actual = Book.objects.get(title=book.title)

        # then
        assert_that(actual).is_equal_to(book)

    def test_that_person_can_be_created(self):
        # given
        person = PersonFactory()

        # when
        actual = Person.people.all()

        # then
        assert_that(actual).contains(person)
