from django.shortcuts import render, redirect
from .forms import CombinedRegistrationForm
from .models import Attendee, Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def combined_registration(request):
    if request.method == 'POST':
        form = CombinedRegistrationForm(request.POST)
        if form.is_valid():
            Attendee.objects.create(
                name=form.cleaned_data['attendee_name'],
                category=form.cleaned_data['category'],
                detail=form.cleaned_data['detail']
            )
            return render(request, 'events/registration_complete.html')
    else:
        form = CombinedRegistrationForm()

    return render(request, 'events/combined_registration.html', {'form': form})



