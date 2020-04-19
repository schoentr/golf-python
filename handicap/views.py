from django.shortcuts import render, get_list_or_404, get_object_or_404,redirect
from .models import Course, Tee
from .forms import EntryForm


# Create your views here
def home_view (request):
  return render(request, 'generic/home.html' ,context={'message':'Tim'})


def course_list_view (request):
  rp=request.POST
  form = EntryForm(request.POST or None)
  courses=  get_list_or_404(Course)
  tees=get_list_or_404(Tee)
  if request.method == 'POST':
    rp1 = rp.copy()
    diff_calculated = calculate_differential(rp1['score'],rp1['tee'])
    rp1['differential'] = str(diff_calculated)
    form=EntryForm(rp1)
    form.save()
    return redirect('user_handicap')
  courses=  get_list_or_404(Course)
  context= {
    'courses':courses,
  }
  return  render (request, 'handicap/courses.html', context)

def user_handicap_view (request):
  name='tim'
  context = {
    'message':name,
  }
  return render(request, 'handicap/user_handicap.html' ,context )

def tee_selection_view (request, pk=None):
  form = EntryForm(request.POST or None)
  if request.method == 'POST' and form.is_valid():
    form.save()
  course = get_object_or_404(Course, id=pk)
  tee = get_list_or_404(Tee, course_id=pk)
  context= {
    'course': course,
    'tees':tee,
    'form':form,
  }
  return render(request,'handicap/tee.html',  context)

def calculate_differential(score,hole_id):
  score= int(score)
  hole_id = int(hole_id)
  tees= Tee.objects.values_list('rating','slope')
  slope= tees[0][1]
  rating = tees[0][0]
  rating=float(rating)
  diff=  (((score - rating) * 113)/slope)
  diff = round(diff,2)
  return diff
