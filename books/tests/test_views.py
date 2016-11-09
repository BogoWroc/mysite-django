from assertpy import assert_that
from django.test import TestCase

from books.views import browser_information
from common.view_testing_tools import get_response_from, verify_that_function_view_is_assigned_to_url


class ViewAsAFunctionTest(TestCase):
    def test_that_view_function_is_assigned_to_dedicated_url(self):
        verify_that_function_view_is_assigned_to_url(browser_information, '/books/browser/')

    def test_that_view_function_returns_correct_response(self):
        response = get_response_from(self.client, browser_information)
        assert_that(response.status_code).is_equal_to(200)

