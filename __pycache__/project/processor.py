from validator import check_record
from utils.decorator import my_decorator


@my_decorator
def process(records):

    # Select valid records
    valid = list(filter(check_record, records))

    # Change usernames to uppercase
    valid = list(map(
        lambda x: x.split()[0].upper() + " "
        + x.split()[1] + " "
        + x.split()[2],
        valid
    ))

    return valid


def get_invalid(records):

    invalid = list(filter(lambda x: not check_record(x), records))

    return invalid