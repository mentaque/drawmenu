from django.shortcuts import render

from drawmenu.models import MenuItem


def menu(request):
    return render(request, 'index.html')


def menu_item(request, item_url):
    menu = MenuItem.objects.get(url=item_url)
    return render(request, 'menu_item.html', {'menu': menu})
