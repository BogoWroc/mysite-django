from assertpy import assert_that
from django.test import TestCase
from django.urls import reverse

from books.views import browser_information, search_form, search
from common.view_testing_tools import get_response_from, verify_that_function_view_is_assigned_to_url, get_content


class ViewAsAFunctionTest(TestCase):
    def test_that_view_function_is_assigned_to_dedicated_url(self):
        verify_that_function_view_is_assigned_to_url(browser_information, '/books/browser/')
        verify_that_function_view_is_assigned_to_url(search_form, '/books/search-form/')
        verify_that_function_view_is_assigned_to_url(search, '/books/search/')

    def test_that_view_function_returns_correct_response(self):
        response = get_response_from(self.client, browser_information)
        assert_that(response.status_code).is_equal_to(200)

        response = get_response_from(self.client, search_form)
        assert_that(response.status_code).is_equal_to(200)

        response = get_response_from(self.client, search)
        assert_that(response.status_code).is_equal_to(200)

    def test_that_proper_message_will_be_returned_when_empty_form_was_sent(self):
        response = self.client.get(
            reverse('search'),
            data={
                'fsearch': ""
            }
        )

        assert_that(get_content(response)).is_equal_to("You submitted an empty form.")

    def test_that_proper_message_will_be_returned_when_form_was_filled(self):
        response = self.client.get(
            reverse('search'),
            data={
                'fsearch': "TEST"
            }
        )

        assert_that(get_content(response)).is_equal_to("You searched for: 'TEST'")
