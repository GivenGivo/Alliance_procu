from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.core.files import File

def generate_id(user, template_path):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # Customize this part to match your ID template
    c.drawString(100, 750, f"ID for {user.first_name} {user.last_name}")
    c.drawString(100, 730, f"Organization: {user.organization}")
    c.drawString(100, 710, f"Position: {user.position}")
    c.drawString(100, 690, f"NRC: {user.nrc}")
    
    c.save()
    buffer.seek(0)
    return File(buffer, name=f"id_{user.id}.pdf")


def generate_certificate(user, template_path):  # Fixed function name
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # Customize this part to match your certificate template
    c.drawString(100, 750, f"Certificate for {user.first_name} {user.last_name}")
    c.drawString(100, 730, f"Organization: {user.organization}")
    c.drawString(100, 710, f"Position: {user.position}")
    
    c.save()
    buffer.seek(0)
    return File(buffer, name=f"certificate_{user.id}.pdf")