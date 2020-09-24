from django.urls import path
from . import views

# Namespace
app_name = 'app'

urlpatterns = [
    # "/app"
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/favorite/', views.favorite, name='favorite')
]
