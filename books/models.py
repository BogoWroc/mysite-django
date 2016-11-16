from django.db import models


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    # Mark field as optional and change field label at admin page to e-mail
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __repr__(self):
        return "first_name = {}, last_name = {}, email = {}".format(
            self.first_name,
            self.last_name,
            self.email
        )


class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)
    objects = BookManager()

    def __str__(self):
        return self.title


class MaleManager(models.Manager):
    def get_queryset(self):
        return super(MaleManager, self).get_queryset().filter(sex='M')


class FemaleManager(models.Manager):
    def get_queryset(self):
        return super(FemaleManager, self).get_queryset().filter(sex='F')


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1,
                           choices=(
                               ('M', 'Male'),
                               ('F', 'Female')
                           )
                           )
    people = models.Manager()
    men = MaleManager()
    women = FemaleManager()
