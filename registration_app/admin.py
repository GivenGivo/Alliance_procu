from django.utils.html import format_html
import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import GeneratedID, GeneratedCertificate, Registration


# GeneratedIDAdmin class to show ID files and generate preview link
@admin.register(GeneratedID)
class GeneratedIDAdmin(admin.ModelAdmin):
    list_display = ('user', 'id_file', 'generated_at', 'preview_link')

    def preview_link(self, obj):
        return format_html('<a href="{}" target="_blank">Preview</a>', obj.id_file.url)
    preview_link.short_description = 'Preview'


# GeneratedCertificateAdmin class to show certificates and generate preview link
@admin.register(GeneratedCertificate)
class GeneratedCertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'certificate_file', 'generated_at', 'preview_link')

    def preview_link(self, obj):
        return format_html('<a href="{}" target="_blank">Preview</a>', obj.certificate_file.url)
    preview_link.short_description = 'Preview'


# RegistrationAdmin class with CSV download action
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'organization', 'position', 'phone_number')
    actions = ['download_csv']

    def download_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="registrations.csv"'
        writer = csv.writer(response)
        writer.writerow(['First Name', 'Last Name', 'Organization', 'Position', 'Phone Number', 'Email', 'NRC'])
        for user in queryset:
            writer.writerow([user.first_name, user.last_name, user.organization, user.position, user.phone_number, user.email, user.nrc])
        return response
    download_csv.short_description = "Download selected registrations as CSV"
