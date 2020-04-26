import factory


class User(factory.DjangoModelFactory):
    full_name = "Test Person"
    nickname = "Test"
    email = "test.person@example.com"
    phone = "07123456789"

    class Meta:
        model = "core.User"
