import factory

from django.contrib.webdesign import lorem_ipsum

from faker import Factory


fake = Factory.create()


class SalesOrderFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'salesorder.SalesOrder'

    title = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(5, common=False).title())
