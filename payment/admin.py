from django.contrib import admin
from .models import Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','amount','month','deposit_at']
    search_fields = ('user', )

admin.site.register(Payment,PaymentAdmin)
