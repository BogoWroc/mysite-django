from assertpy import assert_that
from django.test import TestCase
from faker import Factory

from basic.forms import ContactForm


class ContactFormTest(TestCase):
    def test_that_form_is_valid(self):
        # given
        contact_form = ContactForm(data={
            'subject': "Subject",
            'message': "Message",
        })

        # when/then
        assert_that(contact_form.is_valid()).is_true()

    def test_that_form_is_invalid(self):
        # given
        contact_form = ContactForm(data={})

        # when/then
        assert_that(contact_form.is_valid()).is_false()
        assert_that(contact_form.has_error('subject', code='required')).is_true()
        assert_that(contact_form.has_error('message', code='required')).is_true()

    def test_that_form_with_subject_longer_than_100_characters_is_invalid(self):
        # given
        factory = Factory.create()
        subject = factory.provider('faker.providers.lorem').text(max_nb_chars=200)
        contact_form = ContactForm(data={
            'subject': subject,
            'message': "Message",
        })

        # when/then
        assert_that(contact_form.is_valid()).is_false()
