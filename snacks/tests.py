from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        purchaser = get_user_model().objects.create(username="tester",password="tester")
        self.purchaser = purchaser
        Snack.objects.create(name="tester", purchaser=purchaser)
        
        self.snack = Snack.objects.create(
            name='test',
            description="test info",
            purchaser = purchaser
        )

    def test_list_page_status_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snacks.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('snacks')
        response = self.client.get(url)
        snack = response.context['snacks']
        self.assertEqual(len(snack), 2)
        self.assertEqual(snack[0].name, "tester")
        self.assertEqual(snack[0].purchaser.username, "tester")

    def test_detail_page_status_code(self):
        url = reverse('snack_details',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('snack_details',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_details.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_create_page_template(self):
        url = reverse('snack_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_create.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_delete_page_template(self):
        url = reverse('snack_delete',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_delete.html')
        self.assertTemplateUsed(response, 'base.html')
        
    def test_update_page_template(self):
        url = reverse('snack_update',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_update.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_snack_create_page_context(self):
        url = reverse('snack_details',args=(1,))
        response = self.client.get(url)
        snack = response.context['snack']
        self.assertEqual(snack.name, "tester")
        self.assertEqual(snack.purchaser.username, "tester")
        
    def test_create_view(self):
        obj={
            'name':"test2",
            'description': "info...",
            'purchaser': self.purchaser.id
        }

        url = reverse('snack_create')
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertRedirects(response, "/snacks/")
        
    def test_update_view(self):
        obj={
            'name':"test2",
            'description': "info...",
            'purchaser': self.purchaser.id
        }

        url = reverse('snack_update', args=(1,))
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertRedirects(response, "/snacks/")
        
    def test_delete_view(self):
        obj={
            'name':"test2",
            'description': "info...",
            'purchaser': self.purchaser.id
        }

        url = reverse('snack_delete', args=(1,))
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertRedirects(response, "/snacks/")