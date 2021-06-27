# python
import time
from datetime import datetime, timedelta

# https://docs.python.org/3/library/datetime.html
# If optional argument tz is None or not specified, the timestamp is converted to the platform's local date and time, and the returned datetime object is naive.
# time.mktime(dt.timetuple())


def date_to_timestamp(dt):
    # local timezone to timestamp support python2 pytohn3
    return time.mktime(dt.timetuple())


def get_expiration_time(timestamp, duration):
    #
    now_date = datetime.fromtimestamp(timestamp)
    exp_date = now_date.replace(second=0, microsecond=0)
    if (int(date_to_timestamp(exp_date + timedelta(minutes=1)))
            - timestamp) > 30:
        exp_date = exp_date + timedelta(minutes=1)

    else:
        exp_date = exp_date + timedelta(minutes=2)
    exp = []
    for _ in range(5):
        exp.append(date_to_timestamp(exp_date))
        exp_date = exp_date + timedelta(minutes=1)

    idx = 50
    index = 0
    now_date = datetime.fromtimestamp(timestamp)
    exp_date = now_date.replace(second=0, microsecond=0)
    while index < idx:
        if (int(exp_date.strftime("%M")) % 15 == 0
                and (int(date_to_timestamp(exp_date)) - int(timestamp)) > 60 * 5):
            exp.append(date_to_timestamp(exp_date))
            index = index + 1
        exp_date = exp_date + timedelta(minutes=1)

    remaning = []

    for t in exp:
        remaning.append(int(t) - int(time.time()))

    close = [abs(x - 60 * duration) for x in remaning]

    return int(exp[close.index(min(close))]), int(close.index(min(close)))


def get_remaning_time(timestamp):
    now_date = datetime.fromtimestamp(timestamp)
    exp_date = now_date.replace(second=0, microsecond=0)
    if (int(date_to_timestamp(exp_date + timedelta(minutes=1)))
            - timestamp) > 30:
        exp_date = exp_date + timedelta(minutes=1)

    else:
        exp_date = exp_date + timedelta(minutes=2)
    exp = []
    for _ in range(5):
        exp.append(date_to_timestamp(exp_date))
        exp_date = exp_date + timedelta(minutes=1)
    idx = 11
    index = 0
    now_date = datetime.fromtimestamp(timestamp)
    exp_date = now_date.replace(second=0, microsecond=0)
    while index < idx:
        if (int(exp_date.strftime("%M")) % 15 == 0
                and (int(date_to_timestamp(exp_date)) - int(timestamp)) > 60 * 5):
            exp.append(date_to_timestamp(exp_date))
            index = index + 1
        exp_date = exp_date + timedelta(minutes=1)

    remaning = []

    for idx, t in enumerate(exp):
        if idx >= 5:
            dr = 15 * (idx - 4)
        else:
            dr = idx + 1
        remaning.append((dr, int(t) - int(time.time())))

    return remaning
