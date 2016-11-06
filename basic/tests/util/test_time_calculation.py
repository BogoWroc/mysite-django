import datetime
import unittest

from assertpy import assert_that

from basic.util import time_calculation


class AddHoursTest(unittest.TestCase):
    def test_that_two_hours_was_added(self):
        # given
        time = datetime.datetime(year=2016, month=11, day=6, hour=12)

        # when
        actual_date_time = time_calculation.add_hours(time, 2)

        # then
        assert_that(actual_date_time.hour).is_equal_to(14)
