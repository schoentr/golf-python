from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Course, Tee
from .forms import EntryForm


# Create your views here
def home_view (request):
  return render(request, 'generic/home.html' ,context={'message':'Tim'})


def user_handicap_view (request):
  name='tim'
  context = {
    'message':name,

  }
  return render(request, 'handicap/user_handicap.html' ,context )

def course_list_view (request):
  rp=request.POST
  form = EntryForm(request.POST or None)
  courses=  get_list_or_404(Course)
  print ('courses*****', courses)
  tees=get_list_or_404(Tee)
  print (tees)
  if request.method == 'POST':
    print ('LN25 ********',tees)
    rp1 = rp.copy()
    print('RP----->>',rp1)

    diff_calculated = calculate_differential(rp1['score'],rp1['tee'])

    rp1['differential'] = str(diff_calculated)
    print (rp1['score'],rp1['tee'])
    form=EntryForm(rp1)
    form.save()
  courses=  get_list_or_404(Course)
  context= {
    'courses':courses,
  }
  return  render (request, 'handicap/courses.html', context)

def tee_selection_view (request, pk=None):
  form = EntryForm(request.POST or None)
  if request.method == 'POST':
    form.save()
  

  course = get_object_or_404(Course, id=pk)
  tee = get_list_or_404(Tee, course_id=pk)
  context= {
    'course': course,
    'tees':tee,
    'form':form,
  }
  return render(request,'handicap/tee.html',  context)
# def course_list_view(request):
#   # courses = get_list_or_404(course)
#   context={
#     'courses':'courses'
#   }
#   return render(request, 'handicap/course_list.html',context)

def calculate_differential(score,hole_id):
  print('Hole_ID --> ', hole_id, type(hole_id))
  score= int(score)
  print('Score ->', score, type(score))
  hole_id = int(hole_id)
  tees= Tee.objects.values_list('rating','slope')
  slope= tees[0][1]
  rating = tees[0][0]
  print('Slope -> ', slope, type(slope))
  rating=float(rating)
  print('Rating -> ',rating, type(rating))
  diff=  (((score - rating) * 113)/slope)
  diff = round(diff,2)
  return diff
