from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'pages/contact.html', context)