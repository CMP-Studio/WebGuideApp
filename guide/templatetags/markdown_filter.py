from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()

@register.filter
@stringfilter
def markdownify(text):
    # safe_mode governs how the function handles raw HTML
    return markdown.markdown(text)
