from django.shortcuts import render
from django.http import HttpResponse
from . import ticketingsystemlogic
from .ticketingsystemlogic import TICKTINGSYSTEM
# Create your views here.


#https://grok.com/chat/500456f5-ba5e-41df-9ae9-9f7940a06703

def homepage(request):
  return render(request, 'index.html')
def staffpage(request):
  return render(request, 'userpage.html')
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