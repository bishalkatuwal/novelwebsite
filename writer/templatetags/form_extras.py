from django import template

register = template.Library()

@register.filter
def addcss(field, css_class):
    return field.as_widget(attrs={"class": css_class})
