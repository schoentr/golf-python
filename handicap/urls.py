from django.urls import path, include
from django.contrib import admin
from .views import course_list_view, user_handicap_view,tee_selection_view,scrape_view


urlpatterns = [
  path('admin/', admin.site.urls),
  path('user_handicap/',user_handicap_view, name='user_handicap'),
  path('courses/',course_list_view, name='course_list_view'),
  path('courses/<int:pk>',tee_selection_view,  name='tee_selection'),
  path('scrape/',scrape_view, name='scrape'),

]