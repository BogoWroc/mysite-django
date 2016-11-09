from assertpy import assert_that
from django.test import TestCase

from basic.views import current_datetime, hello, hours_ahead, order_report
from common.view_testing_tools import get_response_from, verify_that_function_view_is_assigned_to_url


class ViewAsAFunctionTest(TestCase):
    def test_that_view_function_is_assigned_to_dedicated_url(self):
        verify_that_function_view_is_assigned_to_url(hello, '/hello/')
        verify_that_function_view_is_assigned_to_url(current_datetime, '/time/')
        verify_that_function_view_is_assigned_to_url(hours_ahead, '/time/plus/3/')
        verify_that_function_view_is_assigned_to_url(order_report, '/order-report/')

    def test_that_view_function_returns_correct_response(self):
        response = get_response_from(self.client, hello)
        assert_that(self._get_content(response)).is_equal_to("Hello world")

        response = get_response_from(self.client, current_datetime)
        assert_that(self._get_content(response)).contains("It is now")

        response = get_response_from(self.client, hours_ahead, kwargs={'offset': 3})
        assert_that(self._get_content(response)).contains("In 3 hour(s)")

        response = get_response_from(self.client, order_report)
        assert_that(self._get_content(response)).contains("Bogumil", "Car", "Bike", "Pythonic")

    def _get_content(self, response):
        return str(response.content, response.charset)
