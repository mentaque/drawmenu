from django import template
from django.template.loader import get_template
from django.urls import reverse, resolve

from drawmenu.models import MenuItem

register = template.Library()


@register.simple_tag()
def draw_menu(title):

    root = MenuItem.objects.get(name=title)
    def build_submenu(parent):
        children = parent.children.all()
        if children:
            submenu = []
            for child in children:
                child_submenu = build_submenu(child)
                submenu.append({
                    'name': child.name,
                    'url': child.url,
                    'submenu': child_submenu
                })
            return submenu
        else:
            return None

    menu = build_submenu(root)

    template = get_template('layout.html')
    context = {'root': root, 'menu': menu}
    html = template.render(context)
    return html


