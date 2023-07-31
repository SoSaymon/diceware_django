import unittest

from django.forms import forms
from django.test import TestCase

from diceware.forms import DiceWareForm


class DiceWareFormTest(TestCase):
    def test_form_has_fields(self):
        form = DiceWareForm()
        expected = ['word_count', 'separator', 'capitalize']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)

    def test_valid_form(self):
        form = DiceWareForm(data={'word_count': 6, 'separator': '-', 'capitalize': True})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = DiceWareForm(data={'word_count': 6, 'separator': '', 'capitalize': False})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'__all__': ['Cannot capitalize first letter without a separator']})

