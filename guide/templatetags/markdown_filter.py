from django import template
from django.template.defaultfilters import stringfilter
import markdown
import re
from pprint import pprint

register = template.Library()

@register.filter
@stringfilter
def markdownify(text):
    html = re.sub(r'\r*\n',"<br>", text)
    return html

#Done
