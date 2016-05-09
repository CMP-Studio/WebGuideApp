from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()

@register.filter
@stringfilter
def markdownify(text):
    if isinstance(text, str):
        html = markdown.markdown(text)
        return html
    else:
        return None

#Done
