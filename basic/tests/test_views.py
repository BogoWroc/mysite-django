from assertpy import assert_that
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase

from basic.views import current_datetime, hello


class ViewAsAFunctionTest(TestCase):
    def test_that_view_function_is_assigned_to_dedicated_url(self):
        self._verify_that_function_view_is_assigned_to_url(hello, '/hello/')
        self._verify_that_function_view_is_assigned_to_url(current_datetime, '/time/')

    def test_that_view_function_returns_correct_response(self):
        response = self._get_response_from(hello)
        assert_that(self._get_content(response)).is_equal_to("Hello world")

        response = self._get_response_from(current_datetime)
        assert_that(self._get_content(response)).contains("It is now")

    def _get_response_from(self, function_view):
        url = self._reverse_function_view_to_url(function_view)
        response = self.client.get(url)
        return response

    def _verify_that_function_view_is_assigned_to_url(self, function_view, url):
        func = self._resolve_function_view_based_on_url(url)
        assert_that(func).is_equal_to(function_view)

    def _reverse_function_view_to_url(self, function_view):
        return reverse(function_view)

    def _resolve_function_view_based_on_url(self, url):
        return resolve(url).func

    def _get_content(self, response):
        return str(response.content, response.charset)
