from django.shortcuts import render, get_list_or_404, get_object_or_404,redirect
from .models import Course, Tee, Round
from .forms import EntryForm


# Create your views here
def home_view (request):

  return render(request, 'generic/home.html' ,context={'message':'Tim'})


def course_list_view (request):
  rp=request.POST
  form = EntryForm(request.POST or None)
  courses=  get_list_or_404(Course)
  tees=Tee.objects.all()
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
  rounds=list(Round.objects.all().order_by('-date_played')[:20])
  print (rounds)
  context = calculate_handicap(rounds)
 
  return render(request, 'handicap/user_handicap.html' ,context )

def tee_selection_view (request, pk=None):
  form = EntryForm(request.POST or None)
  if request.method == 'POST' and form.is_valid():
    form.save()
  course = get_object_or_404(Course, id=pk)
  tee = Tee.objects.filter(course_id=pk)
  print ('TEE LENGTH___>>>>', len(tee))
  if len(tee)==0:
    tee = None
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
  if diff < 0:
    diff = 0
  return diff
  
def calculate_handicap(rounds):
  handi_ratio=1,1,1,1,1,1,2,2,3,3,4,4,5,5,6,6,7,8,9,10
  length_rounds = len(rounds)
  print ('length Rounds #####', length_rounds)
  diffs = []
  for round in rounds:
    round.used = False
    round.save()
    diffs.append(round.differential)
  diffs.sort()
  print(diffs)
  cut = handi_ratio[length_rounds]
  diffs = diffs[:cut]
  sum_diffs= sum(diffs)
  print(sum_diffs)
  handicap = sum_diffs / len(diffs)
  handicap = float(handicap)
  handicap = handicap * 0.96
  count = 0
  for round in rounds:
    if round.differential in diffs and count < len(diffs):
      print('MADE IT *****', round.score)
      round.used = True
      round.save()
      count +=1
      
  context = {
    'handicap':handicap,
    'rounds':rounds
  }

  return context
