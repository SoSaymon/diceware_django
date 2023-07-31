from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    def test_index_view(self):
        """
        Test that the index view returns a 200 response
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'What is Diceware: A Secure Passphrase Generation Method')
        self.assertTemplateUsed(response, 'index.html')
