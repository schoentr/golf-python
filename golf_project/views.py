from django.shortcuts import render

def home_view (request):
  return render(request, 'generic/home.html' ,context={'message':'Tim'})


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