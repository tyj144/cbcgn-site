# FYI: must register content.templatetags as an installed app

from django import template
from datetime import datetime

register = template.Library()

def is_in_future(date):
	return date > datetime.now().date()

register.filter('is_in_future', is_in_future)