from django.shortcuts import render, get_list_or_404, get_object_or_404,redirect
from .models import Course, Tee, Round
from .forms import EntryForm, UrlForm, CourseForm
from bs4 import BeautifulSoup
import requests


# Create your views here
def home_view (request):

  return render(request, 'generic/home.html' ,context={'message':'Tim'})


def course_list_view (request):
  form1=UrlForm(request.POST or None)
  rp=request.POST
  form = EntryForm(request.POST or None)
  courses= Course.objects.all()
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
    'form':form1,
  }
  return  render (request, 'handicap/courses.html', context)

def user_handicap_view (request):
  rounds=list(Round.objects.all().order_by('-date_played')[:20])
  print (rounds)
  context = calculate_handicap(rounds)
 
  return render(request, 'handicap/user_handicap.html' ,context )

def tee_selection_view (request, pk=None):
  course = get_object_or_404(Course, id=pk)
  tee = Tee.objects.filter(course_id=pk)
  if len(tee)==0:
    tee = None
  context= {
    'course': course,
    'tees':tee,
    
  }
  return render(request,'handicap/tee.html',  context)

def scrape_view(request):
  form= UrlForm(request.POST or None)
  if request.method=='POST':
    form = UrlForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      #now in the object cd, you have the form as a dictionary.
      url_cleaned = cd.get('url')
  page_scrape(url_cleaned)
  context={}
  return redirect('course_list_view')


#Helper Functions
  

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
  diffs = []
  for round in rounds:
    round.used = False
    round.save()
    diffs.append(round.differential)
  diffs.sort()
  cut = handi_ratio[length_rounds]
  diffs = diffs[:cut]
  sum_diffs= sum(diffs)
  handicap = sum_diffs / len(diffs)
  handicap = float(handicap)
  handicap = handicap * 0.96
  count = 0
  for round in rounds:
    if round.differential in diffs and count < len(diffs):
      round.used = True
      round.save()
      count +=1    
  context = {
    'handicap':handicap,
    'rounds':rounds
  }
  return context

def page_scrape(url):
  html_content = requests.get(url).text
  soup = BeautifulSoup(html_content, 'lxml')
  name =soup.find('h3').text
  address = soup.find('span', itemprop='streetAddress').text
  city = soup.find('span', itemprop='addressLocality').text
  region = soup.find ('span', itemprop='addressRegion').text
  zipCode= soup.find ('span', itemprop='postalCode').text
  course = Course(name=name, street=address, city=city,region=region,zip_Code=zipCode)

  course.save()
  course_id=course.id
  
  color=[]
  par=[]
  length=[]
  rating=[]
  slope=[]

  table = soup.find('table',id='course-details-chart')
  tbody = table.find('tbody')
  rows = tbody.find_all('tr')
  for  row in rows:
    color_scraped = row.find_all('td')[0].text
    par_scraped = row.find_all('td')[1].text
    length_scraped = row.find_all('td')[2].text
    rating_scraped = row.find_all('td')[3].text
    slope_scraped = row.find_all('td')[4].text
    tee= Tee(course=course,color=color_scraped,length=length_scraped,rating=rating_scraped,slope=slope_scraped,par=par_scraped)
    tee.save()
    
  print(name, address, city, region, zipCode,'----',course_id)

  return 1
