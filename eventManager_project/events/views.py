from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import EventForm
from django.contrib.auth.models import User
from django.contrib import messages



@login_required
def upcoming_events(request):
    now = timezone.now()
    query = request.GET.get('query', '')  
    
    if request.user.is_staff:
        if query:
            events = Event.objects.filter(name__icontains=query).order_by('start_date')
        else:
            events = Event.objects.all().order_by('start_date')
    else:
        if query:
            events = Event.objects.filter(start_date__gt=now, name__icontains=query).order_by('start_date')
        else:
            events = Event.objects.filter(start_date__gt=now).order_by('start_date')

    return render(request, 'upcoming_events.html', {
        'events': events,
        'now': now
    })

def admin_check(user):
    return user.is_staff

@login_required
@user_passes_test(admin_check)
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('upcoming_events')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


@login_required
@user_passes_test(admin_check)
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, f'Event "{event.name}" has been updated successfully.')
            return redirect('upcoming_events')
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form, 'event': event})


@login_required
@user_passes_test(admin_check)
@require_POST  
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('upcoming_events')


@login_required
def toggle_registration(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user in event.attendees.all():
        event.attendees.remove(request.user)
    else:
        event.attendees.add(request.user)
    return redirect('upcoming_events')


@login_required
def unregister_user(request, event_id, user_id):
    event = get_object_or_404(Event, id=event_id)
    user = get_object_or_404(User, id=user_id)  # Use the imported User model
    if request.user.is_staff:
        event.attendees.remove(user)
    return redirect('upcoming_events')
