import re

def check_record(record):
    try:
        username, email, time = record.split()

        email_pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
        time_pattern = r'^([01][0-9]|2[0-3]):[0-5][0-9]$'

        if re.match(email_pattern, email) and re.match(time_pattern, time):
            return True
        else:
            return False

    except:
        return False