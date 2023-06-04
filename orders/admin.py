from django.contrib import admin
from  .models import  *
# Register your models here.
admin.site.register(Order)
admin.site.register(Offer)
admin.site.register(PrivacyPolicy)
admin.site.register(UserCall)
admin.site.register(ChauffeurCall)