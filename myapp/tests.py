from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import Register

class AppViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_pages_load_successfully(self):
        # Test home page
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

        # Test contact page
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_form_submission(self):
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Hello logistics team'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Thank you! Your inquiry has been submitted successfully.")

    def test_sign_up_get_and_post(self):
        # GET signup page
        response = self.client.get(reverse('Sign_Up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Sign_Up.html')

        # POST signup page
        response = self.client.post(reverse('Sign_Up'), {
            'username': 'john_doe',
            'password': 'password123',
            'name': 'John Doe',
            'age': '25'
        })
        self.assertRedirects(response, reverse('Sign_In'))
        self.assertTrue(Register.objects.filter(username='john_doe').exists())

    def test_role_based_dashboards(self):
        # Create standard user
        user = Register.objects.create_user(username='standard_user', password='password123', name='Standard User', age=25)
        
        # Create admin user
        admin = Register.objects.create_superuser(username='admin_user', password='password123', name='Admin User', age=35)

        # 1. Standard user login -> User Dashboard
        response = self.client.post(reverse('Sign_In'), {
            'username': 'standard_user',
            'password': 'password123'
        })
        self.assertRedirects(response, reverse('user_dashboard'))

        # Standard user accessing admin dashboard -> Redirect to user dashboard
        response = self.client.get(reverse('admin_dashboard'))
        self.assertRedirects(response, reverse('user_dashboard'))
        
        self.client.get(reverse('logout'))

        # 2. Admin user login -> Admin Dashboard
        response = self.client.post(reverse('Sign_In'), {
            'username': 'admin_user',
            'password': 'password123'
        })
        self.assertRedirects(response, reverse('admin_dashboard'))

        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_dashboard.html')

        # Logout
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('Sign_In'))
