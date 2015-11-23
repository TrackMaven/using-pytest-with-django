from example.models import Dog
import pytest


# If your tests need to use the database and want to use pytest
# function test approach, you need to `mark` it.
@pytest.mark.django_db
def test_save():
    maven = Dog(name="Maven", breed="corgi")
    maven.save()
    assert maven.name == "Maven"
    assert maven.breed == "corgi"


# Any existing `unittest` style tests still work without any changes needed.
from django.test import TestCase


class ExampleTestCase(TestCase):
    def setUp(self):
        self.maven = Dog(name="Maven", breed="corgi")
        self.maven.save()

    def test_save(self):
        self.assertEquals(self.maven.name, "Maven")
        # You can mix in pytest's `assert` approach!
        assert self.maven.breed == "corgi"
