import datetime


def add_hours(time, hours_to_add):
    """
    :param time: timedate
    :param hours_to_add: int
    :return: timedate
    """
    return time + datetime.timedelta(hours=hours_to_add)
