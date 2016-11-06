from django.http import Http404


def convert_str_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise Http404("Value '%s' is not an int number!".format(value))
