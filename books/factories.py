import factory
from django.utils.timezone import now

from books.models import Author, Book, Publisher


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher

    name = factory.Faker('name')
    address = factory.Faker('address')
    city = factory.Faker('city')
    state_province = factory.Faker('state')
    country = factory.Faker('country')
    website = factory.Faker('url')


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('word')
    publisher = factory.SubFactory(PublisherFactory)
    publication_date = now()

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for authors in extracted:
                self.authors.add(authors)
