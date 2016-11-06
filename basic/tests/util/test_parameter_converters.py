import unittest

from assertpy import assert_that
from assertpy import fail
from django.http import Http404

from basic.util.parameter_converters import convert_str_to_int


class ConvertStringToIntTest(unittest.TestCase):
    def test_that_value_is_converted_to_int(self):
        actual = convert_str_to_int("12")
        assert_that(actual).is_equal_to(12)

    def test_that_error_is_reported_when_value_is_not_a_int_number(self):
        try:
            convert_str_to_int("a")
            fail("It should report an error.")
        except Http404 as e:
            assert_that(e).is_not_none()
