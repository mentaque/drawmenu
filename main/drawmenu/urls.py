from django.urls import path

from drawmenu.views import menu, menu_item

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('menu/<slug:item_url>', menu_item, name='menu_item')
]