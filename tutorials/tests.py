from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial

# Create your tests here.
def test_homepage_accss():
    url = reverse('home')
    assert url == "/"

# @pytest.mark.django_db
# def test_create_tutorial():
#     tutorial = Tutorial.objects.create(
#             title='Pytest',
#             tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
#             description='Tutorial on ho wto apply pytest to a Django application',
#             published=True
#         )
#     assert tutorial.title == 'Pytest'


@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial
