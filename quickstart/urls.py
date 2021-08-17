from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'items', views.ItemListView)
router.register(r'lists', views.ShoppingListView)

urlpatterns = [
    path('', include(router.urls)),
]
