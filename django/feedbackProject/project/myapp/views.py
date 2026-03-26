from django.shortcuts import render, redirect
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

        return redirect('home')   # reload page

    feedbacks = Feedback.objects.all().order_by('-id')

    return render(request, 'home.html', {'feedbacks': feedbacks})


def delete_feedback(request, id):
    feedback = Feedback.objects.get(id=id)
    feedback.delete()
    return redirect('home')