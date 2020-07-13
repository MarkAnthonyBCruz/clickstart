from django.urls import include, path
from . import views

app_name = "newsapp"

urlpatterns = [
    path('', views.news, name = "news_home"),
    path('bbc/', views.bbc, name = "bbc"),
    path('wsj/', views.tws, name = "wsj"),
    path('corona/', views.corona, name = "corona"),
]