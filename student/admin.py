from django.contrib import admin
from .models import Reg
from django.core.mail import send_mail
from django.conf import settings

class RegAdmin(admin.ModelAdmin):
    # ... other fields and configurations

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if not change:  # Execute only when a new object is added
            subject = 'Welcome to Our Website!'
            message = f"Dear {obj.username},\n\nThank you for registering on our website. We hope you enjoy your experience!"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [obj.email]
            send_mail(subject, message, from_email, recipient_list)

admin.site.register(Reg, RegAdmin)
