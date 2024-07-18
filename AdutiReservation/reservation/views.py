# views.py

from django.shortcuts import render, redirect
from .forms import ReservationForm

def reserver_place(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservation_form.html', {'form': form})

def reservation_success(request):
    return render(request, 'reservation_success.html')
