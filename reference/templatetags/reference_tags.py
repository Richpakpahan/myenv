from django import template
from ..models import Reference
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag()
def total_references():
    return Reference.objects.count()

@register.inclusion_tag('reference/post/latest_references.html')
def show_latest_references(count=5):
    latest_references = Reference.objects.order_by('-created')[:count]
    return {'latest_references': latest_references}

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))