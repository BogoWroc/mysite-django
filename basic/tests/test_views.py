from assertpy import assert_that
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase

from basic.views import hello


class ViewAsAFunctionTest(TestCase):
    def test_that_view_function_is_assigned_to_dedicated_url(self):
        func = self._resolve_function_view_based_on_url()
        assert_that(func).is_equal_to(hello)

    def test_that_view_function_returns_correct_response(self):
        url = self._reverse_function_view_to_url()
        response = self.client.get(url)
        assert_that(self._get_content(response)).is_equal_to("Hello world")

    def _reverse_function_view_to_url(self):
        return reverse(hello)

    def _resolve_function_view_based_on_url(self):
        return resolve('/hello/').func

    def _get_content(self, response):
        return str(response.content, response.charset)
