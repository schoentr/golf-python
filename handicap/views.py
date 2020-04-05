from django.shortcuts import render, get_list_or_404


# Create your views here

def course_list_view(request):
  courses = get_list_or_404(course)
  context={
    'courses':'courses'
  }
  return render(request, ' course/course_list.html',context)

def course_detail_view(request, pk=none):
  context = {
    'course':get_object_or_404(course,  id=pk)
  }
  return render (request, 'courses/course_detail.html', context)