from . import views
from django.urls import path


urlpatterns = [
    path('example/', views.example, name='example'),
    path('update_demographics/<id>', views.update_demographics, name='update_demographics'),
    # path('example/', views.example, name='example'),
    # path('sample-post/', views.sample_post, name='sample-post'),
]