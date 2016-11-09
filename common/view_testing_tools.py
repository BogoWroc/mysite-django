from assertpy import assert_that
from django.urls import resolve, reverse


def get_response_from(client, function_view, **kwargs):
    url = _reverse_function_view_to_url(function_view, **kwargs)
    response = client.get(url)
    return response


def verify_that_function_view_is_assigned_to_url(function_view, url):
    func = _resolve_function_view_based_on_url(url)
    assert_that(func).is_equal_to(function_view)


def _reverse_function_view_to_url(function_view, **kwargs):
    return reverse(function_view, **kwargs)


def _resolve_function_view_based_on_url(url):
    return resolve(url).func
