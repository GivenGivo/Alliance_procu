from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration, GeneratedID, GeneratedCertificate
from .utils import generate_id, generate_certificate  # Ensure the correct function name is imported

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            
            # Generate ID
            id_file = generate_id(user, 'path/to/id_template.pdf')
            GeneratedID.objects.create(user=user, id_file=id_file)
            
            # Generate Certificate
            certificate_file = generate_certificate(user, 'path/to/certificate_template.pdf')  # Fixed function name
            GeneratedCertificate.objects.create(user=user, certificate_file=certificate_file)
            
            return redirect('success', first_name=user.first_name)
    else:
        form = RegistrationForm()
    return render(request, 'registration_app/register.html', {'form': form})

def success(request, first_name):
    return render(request, 'registration_app/success.html', {'first_name': first_name})