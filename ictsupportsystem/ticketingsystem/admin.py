from django.contrib import admin
from .models import Ticket
from django.utils.html import format_html
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.contrib.admin import ModelAdmin
from django import forms
from .forms import PriorityForm
# Register your models here.



@admin.action(description='Change status')
def changeStatus(modeladmin, request, queryset):
  updated = queryset.update(status='resolved')
  #messages.success(request, f"{updated} ticket(s) marked as resolved.")
  modeladmin.message_user(request, f"{updated} tickets marked as resolved.")
  return

@admin.action(description='Assign agent')
def assignAgent(modeladmin, request, queryset):
  updated = queryset.update(agent='oficer')
  modeladmin.message_user(request, f"{updated} Agent assinged")
  return

@admin.action(description='Change priority level')
def changePriorityLevel(modeladmin, request, queryset):
   
#""pdated = queryset.update(priority='medium')
 #modeladmin.message_user(request, f"{updated} priority changed.")
 #return"""
  form = None

  if 'apply' in request.POST:
    form = PriorityForm(request.POST)
    if form.is_valid():
       priority = form.cleaned_data['priority']
       count = queryset.update(priority=priority)
       modeladmin.message_user(request, f"{count} items updated to priority '{priority}'.")
       redirect(request.get_full_path())

  if not form:
    form = PriorityForm(initial={
      '_selected_action': request.POST.getlist(ACTION_CHECKBOX_NAME)
    })

  return render(request, 'admin/change_priority.html', {
        'items': queryset,
        'form': form,
        'title': 'Change Priority Level'
    })

class TicketAdmin(admin.ModelAdmin):
    list_display = ('tId', 'title', 'description', 'category','priority' ,'status','agent' ,'creationDateTime')
    actions = [changeStatus, assignAgent, changePriorityLevel] 

admin.site.register(Ticket, TicketAdmin)