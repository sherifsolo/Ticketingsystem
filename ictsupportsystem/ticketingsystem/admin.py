from django.contrib import admin
from .models import Ticket
from django.utils.html import format_html
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.contrib.admin import ModelAdmin
from django import forms
from .forms import PriorityForm, StatusForm, AgentForm
# Register your models here.



@admin.action(description='Change status')
def changeStatus(modeladmin, request, queryset):
  form = None

  if 'apply' in request.POST:
    form = StatusForm(request.POST)
    if form.is_valid():
       status = form.cleaned_data['status']
       selected = request.POST.getlist('_selected_action')
       queryset = modeladmin.model.objects.filter(pk__in = selected)
       count = queryset.update(status=status)
       modeladmin.message_user(request, f"{count} items status updated to '{status}'.")
       return redirect(request.get_full_path())

  if not form:       
    form = StatusForm(initial={
      '_selected_action': request.POST.getlist(ACTION_CHECKBOX_NAME)
    })

  return render(request, 'admin/statusform.html', {
        'items': queryset,
        'form': form,
        'title': 'change status'
    })

@admin.action(description='Assign agent')
def assignAgent(modeladmin, request, queryset):
  form = None

  if 'apply' in request.POST:
    form = AgentForm(request.POST)
    if form.is_valid():
       agent = form.cleaned_data['agents']
       selected = request.POST.getlist('_selected_action')
       queryset = modeladmin.model.objects.filter(pk__in = selected)
       count = queryset.update(agent=agent)
       modeladmin.message_user(request, f"{count} items agent updated to '{agent}'.")
       return redirect(request.get_full_path())

  if not form:       
    form = AgentForm(initial={
      '_selected_action': request.POST.getlist(ACTION_CHECKBOX_NAME)
    })

  return render(request, 'admin/agentform.html', {
        'items': queryset,
        'form': form,
        'title': 'Assign Agent'
    })
@admin.action(description='Change priority level')
def changePriorityLevel(modeladmin, request, queryset):
    form = None

    if 'apply' in request.POST:
        form = PriorityForm(request.POST)
        if form.is_valid():
            priority = form.cleaned_data['priority']
            selected = request.POST.getlist('_selected_action')
            queryset = modeladmin.model.objects.filter(pk__in=selected)
            count = queryset.update(priority=priority)
            modeladmin.message_user(request, f"{count} items updated to priority '{priority}'.")
            return redirect(request.get_full_path())

    if not form:
        form = PriorityForm(initial={
            '_selected_action': request.POST.getlist(ACTION_CHECKBOX_NAME)
        })

    return render(request, 'admin/priorityform.html', {
        'items': queryset,
        'form': form,
        'title': 'Change Priority Level'
    })
class TicketAdmin(admin.ModelAdmin):
    list_display = ('tId', 'title', 'description', 'category','priority' ,'status','agent' , 'owner','creationDateTime')
    actions = [changeStatus, assignAgent, changePriorityLevel] 

admin.site.register(Ticket, TicketAdmin)