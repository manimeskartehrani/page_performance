from datetime import date
import calendar
from datetime import timedelta

# from constant_data import today


def check_date_condition(todayDate):
    if (todayDate.day < 28 and todayDate.day > 1):
        if (todayDate.month - 1 == 0):
            todayDate = date(todayDate.year-1,
                             todayDate.month + 11, todayDate.day)
            current_month(todayDate)
            pre_month(todayDate)

        else:
            todayDate = date(
                todayDate.year, todayDate.month - 1, todayDate.day)
            current_month(todayDate)
            pre_month(todayDate)

            return current_month(todayDate), pre_month(todayDate)

    if (todayDate.day == 1):

        if (todayDate.month - 1 == 0):
            todayDate = date(todayDate.year-1,
                             todayDate.month + 11, todayDate.day)

        else:
            todayDate = date(
                todayDate.year, todayDate.month - 1, todayDate.day)

        current_month(todayDate)
        pre_month(todayDate)

        return current_month(todayDate), pre_month(todayDate)

    else:
        return current_month(todayDate), pre_month(todayDate)


def current_month(todayDate):
    month_range = calendar.monthrange(todayDate.year, todayDate.month)

    if (todayDate.day >= 28 and todayDate.day < 32):
        end_of_month = todayDate.replace(
            day=todayDate.day).strftime("%Y-%m-%d")
    else:
        end_of_month = todayDate.replace(
            day=month_range[1]).strftime("%Y-%m-%d")

    start_of_month = (todayDate).replace(day=1).strftime("%Y-%m-%d")
    month_name = todayDate.replace(day=month_range[1]).strftime("%B")

    return [start_of_month, end_of_month, month_name]


def pre_month(todayDate):

    month_range = calendar.monthrange(todayDate.year, todayDate.month)

    if (todayDate.day >= 28 and todayDate.day < 32):
        end_of_pre_month = (todayDate.replace(
            day=todayDate.day) - timedelta(days=31)).strftime("%Y-%m-%d")
    else:
        end_of_pre_month = (todayDate.replace(day=1) -
                            timedelta(days=1)).strftime("%Y-%m-%d")

    start_of_pre_month = (
        todayDate - timedelta(days=todayDate.day)).replace(day=1).strftime("%Y-%m-%d")
    # end_of_pre_month = (todayDate.replace(day=1) - timedelta(days=1)).strftime("%Y-%m-%d")
    month_name = (todayDate.replace(day=1) - timedelta(days=1)).strftime("%B")
    return [start_of_pre_month, end_of_pre_month, month_name]
