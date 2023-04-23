from django.contrib import admin
from first_app.models import Topic, AccessRecord, WebPage, Users
# Register your models here.
admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(Users)
