import factory
from django.utils.timezone import now
from faker.providers import BaseProvider

from books.models import Author, Book, Publisher, Person


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


class SexProvider(BaseProvider):
    __provider__ = "sex"
    __lang__ = "en_US"

    _sex = [
        u'Male', u'Female',
    ]

    @classmethod
    def sex(cls):
        return cls.random_element(cls._sex)


factory.Faker.add_provider(SexProvider)

class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    sex = factory.Faker('sex')
