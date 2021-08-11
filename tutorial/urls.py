from django.urls import include, path
from quickstart import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/items/<int:pk>/', views.ShopItemView.as_view()),
    path('api/items/', views.ShopItemListView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
