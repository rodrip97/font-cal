from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import ContactForm


def index(request):
    return render(request, 'front/index.html')


def about(request):
    return render(request, 'front/about_us.html')


def portfolio(request):
    return render(request, 'front/portfolio.html')


def calendar(request):
    return render(request, 'front/calendar.html')


def contact(request):
    if request.method == 'POSt':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com',['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found.')
            return redirect('front/index')

    form = ContactForm()
    return render(request, 'front/contact.html', {'form':form})








