from django.shortcuts import render
from django.contrib.auth import authenticate, login

def home_view (request):
  if request.user.is_authenticated:
    current_one=request.user
    leng_name=len(current_one.first_name)
    if leng_name > 0:
      name = request.user.first_name
    else:
      name  = current_one.username
    message = 'Welcome back ' + name
  else:
    message = 'Please sign in or register.'
  return render(request, 'generic/home.html' ,context={'message':message})


def user_handicap_view (request):

  name='tim'
  context = {
    'message':name,
  }
  return render(request, 'generic/user_handicap.html' ,context )

def course_list_view (request):
  context= {
    'courses':{'name':'White Hourse'}
  }
  return  render (request, 'generic/courses.html', context)