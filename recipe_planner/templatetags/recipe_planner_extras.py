from django import template
import datetime

register = template.Library()

# https://stackoverflow.com/questions/24818768/django-built-in-timesince-filter-to-show-only-days
@register.filter(expects_localtime=True)
def days_since(value, arg=None):
    try:
        tzinfo = getattr(value, 'tzinfo', None)
        value = datetime.date(value.year, value.month, value.day)
    except AttributeError:
        # Passed value wasn't a date object
        return value
    except ValueError:
        # Date arguments out of range
        return value
    today = datetime.datetime.now(tzinfo).date()
    delta = value - today
    day_str = "days ago"

    # if abs(delta.days) == 1:
    #     day_str = _("day")
    # else:
    #     day_str = _("days")

    # if delta.days < 1:
    #     fa_str = _("ago")
    # else:
    #     fa_str = _("from now")

    return "%03d%s" % (abs(delta.days), day_str)
