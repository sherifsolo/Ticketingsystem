from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.shortcuts import redirect
from ticketingsystem.models import Ticket
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, get_user_model
from django.urls import reverse
from .forms import MyUserCreationForm

# Create your views here.


#https://grok.com/chat/500456f5-ba5e-41df-9ae9-9f7940a06703
def homepage(request):
  return render(request, 'index.html')

@login_required 
def staffpage(request):
  if request.user.is_authenticated:
     if request.user.is_superuser:
        return redirect(reverse('admin:index'))
  return render(request, 'userpage.html')

#sanitize user input to prevent sql injection, xss


def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = MyUserCreationForm()
    return render(request, 'registration/signupform.html', {'form': form})

def dashboard(request):
    return render(request, 'index.html')

@login_required 
def ticketCreationHandler(request):
  if request.method != 'POST':
    return redirect('/')
  title = request.POST.get('title')
  description = request.POST.get('description')
  category = request.POST.get('category')
  priority = request.POST.get('priority')
  uploads = request.POST.get('uploads')
  owner = ""
  if request.user.is_authenticated:
        Users = get_user_model()
        username = request.user.username
        user = Users.objects.get(username=username)
        owner = user
        
  try:
    import time
    import math
  except ImportError as e:
          print(f"failed to import the time module with error {e}\n please make sure its installed")
  except Exception as e:
    print("An unexpected error occured...this tickets id has been set to 0, set it manually to avoid collision")
  Id = 0
  currentTime = time.time()
  timeString = time.ctime()
  checkSum = 0
  for char in title:
    checkSum += ord(char) #gets the ascii value of ech digit and adds it to our checksum.
    checkSum += 1
              #print(f"current time {currentTime} on {timeString}\n ")
              #print(f"Current time plus checksum = {currentTime + checkSum}")
  iD = currentTime + checkSum 
  iD = math.ceil((iD % 365)) 
              #Tue Jun  3 08:38:01 2025
              #123456789012

  id = f"{timeString[0]}{timeString[4]}{timeString[9]}{str(iD)}"
  Id = id
  
  data = Ticket.objects.create(
    tId = Id, 
    title = title, 
    description = description, 
    category = category, 
    priority=priority, 
    uploads = uploads, 
    status = "open", 
    agent = "ictlabour",
    owner = owner,
    )
  print(data)
  return HttpResponse(f"your ticket with this details was submitted:::: id:{Id} title:{title} \n description:{description} \ncategory:{category} \npriority:{priority} \nuploads:{uploads} \n")
