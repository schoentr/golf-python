from django.urls import path
from .views import course_list_view, course_detail_view


urlpatterns = [

  path('',course_list_view,name='course_list_view'),
  path('<int:pk>',course_detail_view,name='course_detail_view'),
]