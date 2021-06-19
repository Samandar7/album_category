from django.urls import path
from .views import HomePageView,PhotoDetailView,ListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/', PhotoDetailView.as_view(), name='detail'),
    path('list/', ListView.as_view(), name='list'),
]
