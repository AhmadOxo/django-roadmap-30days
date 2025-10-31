import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def auth_client(api_client):
    user = User.objects.create_user(username='testuser', password='1234')
    api_client.force_authenticate(user=user)
    return api_client

@pytest.mark.django_db
def test_create_post(auth_client):
    response = auth_client.post('/api/posts/', {
        'title': 'Test Post',
        'content': 'Hello from pytest!'
    })
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == 'Test Post'