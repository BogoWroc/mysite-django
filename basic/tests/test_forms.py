from assertpy import assert_that
from django.test import TestCase

from basic.forms import ContactForm


class ContactFormTest(TestCase):
    def test_that_form_is_valid(self):
        contact_form = ContactForm(data={
            'subject': "Subject",
            'message': "Message",
        })

        assert_that(contact_form.is_valid()).is_true()

    def test_that_form_is_invalid(self):
        contact_form = ContactForm(data={})
        assert_that(contact_form.is_valid()).is_false()
        assert_that(contact_form.has_error('subject', code='required')).is_true()
        assert_that(contact_form.has_error('message', code='required')).is_true()
