from django.shortcuts import render
from django.http import HttpResponse
from . import ticketingsystemlogic
from .ticketingsystemlogic import TICKTINGSYSTEM
from django.shortcuts import redirect
# Create your views here.


#https://grok.com/chat/500456f5-ba5e-41df-9ae9-9f7940a06703

def homepage(request):
  return render(request, 'index.html')
def staffpage(request):
  return render(request, 'userpage.html')

#sanitize user input to prevent sql injection, xss
def login(request):
  if request.method == 'POST':
    user = request.POST.get('username')
    password = request.POST.get('password')
    if user == "" or password == "":
      error = "Password or username is required"
    if user == "admin" and password == "admin024":
        return redirect('/admin/')
    elif user == "staff" and password == "staff097":
        return render(request, 'userpage.html')
    else:
      error = f"invalid username {user} or password {password}"
      return render(request, 'userpage.html',{'error': error} )
    
def ticketCreationHandler(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    description = request.POST.get('description')
    category = request.POST.get('category')
    priority = request.POST.get('priority')
    uploads = request.POST.get('uploads')

    
  ts = TICKTINGSYSTEM()

  ticket = ts.createTicket(title, description, category, priority, uploads)
  return HttpResponse(f"your ticket with this details was submitted:::: id:{ticket[0]} title:{ticket[1]} \n description:{ticket[2]} \ncategory:{ticket[3]} \npriority:{ticket[4]} \nuploads:{ticket[5]} \n")

  return render(request, 'userpage.html')