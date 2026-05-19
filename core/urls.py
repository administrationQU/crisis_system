from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('category/<int:category_id>/', views.topics, name='topics'),

    path('protocol/<int:topic_id>/', views.protocol_view, name='protocol'),

    path('search/', views.search, name='search'),

    path('about/', views.about, name='about'),
]