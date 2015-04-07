from django import template

register = template.Library()

@register.filter(name='addcss')
def addcss(field, value, attr='class'):
    return field.as_widget(attrs={attr: value})

@register.filter(name='get_value')
def addcss(values, key):
    value = [v.value for v in values if v.section_field.slug == key]
    if len(value) > 0:
        return value[0]
    return ''