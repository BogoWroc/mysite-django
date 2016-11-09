from assertpy import assert_that
from django.test import TestCase
from django.urls import reverse

from books.factories import BookFactory
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

        assert_that(get_content(response)).is_equal_to("Please submit a search term.")


class SearchViewTest(TestCase):
    def setUp(self):
        self.book1 = BookFactory(title="Title1")
        self.book2 = BookFactory(title="Title2")
        self.book3 = BookFactory(title="Other")

    def test_that_list_of_books_with_title_started_from_selected_prefix_will_be_displayed(self):
        response = self.client.get(
            reverse('search'),
            data={
                'fsearch': "Title"
            }
        )

        assert_that(get_content(response)).contains("Title1", "Title2")

    def test_that_any_book_match_to_dedicated_search(self):
        response = self.client.get(
            reverse('search'),
            data={
                'fsearch': "New"
            }
        )

        assert_that(get_content(response)).contains("No books matched your search criteria.")
