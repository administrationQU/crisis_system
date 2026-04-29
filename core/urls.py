from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.topics, name='topics'),
    path('topic/<int:topic_id>/', views.choose_role, name='choose_role'),
    path('protocol/<int:topic_id>/<str:role>/', views.protocol_view, name='protocol'),
    path('search/', views.search, name='search'),
]