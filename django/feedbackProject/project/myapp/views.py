from django.shortcuts import render
from .models import Feedback

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Feedback.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, 'home.html', {'success': True})

    return render(request, 'home.html')