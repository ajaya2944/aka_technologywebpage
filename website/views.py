from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    # Your contact form code (if you have one) or just render the template
    return render(request, 'contact.html')

def contact_success(request):
    return render(request, 'contact_success.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                f'Contact Form Submission from {name}',
                f'Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}',
                'your-email@example.com',  # Replace with your email (sender email)
                ['a.k.a2023technology@gmail.com'],  # Replace with your email (receiver email)
                fail_silently=False,
            )
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
