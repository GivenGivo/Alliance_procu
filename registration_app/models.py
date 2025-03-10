from django.db import models

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    picture = models.ImageField(upload_to='images/')
    nrc = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class IDTemplate(models.Model):
    name = models.CharField(max_length=100)
    template_file = models.FileField(upload_to='id_templates/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CertificateTemplate(models.Model):
    name = models.CharField(max_length=100)
    template_file = models.FileField(upload_to='certificate_templates/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class GeneratedID(models.Model):
    user = models.OneToOneField(Registration, on_delete=models.CASCADE)
    id_file = models.FileField(upload_to='generated_ids/')
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID for {self.user.first_name} {self.user.last_name}"


class GeneratedCertificate(models.Model):
    user = models.OneToOneField(Registration, on_delete=models.CASCADE)
    certificate_file = models.FileField(upload_to='generated_certificates/')
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Certificate for {self.user.first_name} {self.user.last_name}"