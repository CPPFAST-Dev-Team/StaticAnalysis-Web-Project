# Not yet implemented in the project
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer, UserSerializer

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.project = Project.objects.create(
            name='Test Project',
            description='A test project description',
            owner=self.user
        )

    def test_user_registration(self):
        """Test user registration"""
        url = reverse('user-register')
        data = {'username': 'newuser', 'password': 'newpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('token' in response.data)

    def test_user_login(self):
        """Test user login"""
        url = reverse('user-login')
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_project_list(self):
        """Test retrieving a list of projects"""
        url = reverse('project-list')
        response = self.client.get(url)
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_project_create(self):
        """Test creating a new project"""
        url = reverse('project-list')
        data = {'name': 'New Project', 'description': 'A new test project'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 2)
        self.assertEqual(Project.objects.get(name='New Project').description, 'A new test project')

    def test_project_detail(self):
        """Test retrieving details of a project"""
        url = reverse('project-detail', kwargs={'pk': self.project.id})
        response = self.client.get(url)
        serializer = ProjectSerializer(self.project)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_project_update(self):
        """Test updating a project"""
        url = reverse('project-detail', kwargs={'pk': self.project.id})
        data = {'name': 'Updated Project', 'description': 'Updated description'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, 'Updated Project')
        self.assertEqual(self.project.description, 'Updated description')

    def test_project_delete(self):
        """Test deleting a project"""
        url = reverse('project-detail', kwargs={'pk': self.project.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Project.objects.count(), 0)

    def test_unauthorized_access(self):
        """Test that unauthorized users cannot access protected endpoints"""
        self.client.force_authenticate(user=None)
        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_project_create_invalid_data(self):
        """Test creating a project with invalid data"""
        url = reverse('project-list')
        data = {'name': ''}  # Invalid: empty name
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_project_update_invalid_data(self):
        """Test updating a project with invalid data"""
        url = reverse('project-detail', kwargs={'pk': self.project.id})
        data = {'name': ''}  # Invalid: empty name
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_project_list_ordering(self):
        """Test that projects are returned in the correct order"""
        Project.objects.create(name='Project B', owner=self.user)
        Project.objects.create(name='Project A', owner=self.user)
        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Project A')
        self.assertEqual(response.data[1]['name'], 'Project B')
        self.assertEqual(response.data[2]['name'], 'Test Project')