import simplejson as json
from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter(name='addcss')
def addcss(field, value, attr='class'):
    return field.as_widget(attrs={attr: value})

@register.filter(name='get_value')
def get_value(values, key):
    value = [v.value for v in values if v.section_field.slug == key]
    if len(value) > 0:
        return value[0]
    return ''

@register.filter(name='get_description')
def get_description(display):
    return display.descriptions.order_by('-date_created').first()

@register.filter(name='get_descr_value')
def get_descr_value(description, key):
    if description == None:
        return ''
    value = [v.value for v in description.values.all() if v.section_field.slug == key]
    if len(value) > 0:
        return value[0]
    return ''


@register.filter(name='display_json')
def display_json(displays):
    # def serialize_position(position):
    #   return str(d.position)

    return mark_safe(json.dumps([{
            'id': d.id,
            'title': d.title,
            'position': str(d.position)
            } for d in displays], separators=(',', ': ')))