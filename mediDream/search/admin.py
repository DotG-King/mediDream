from django.contrib import admin
from accounts.models import MEMBERS
from list.models import Search_History, DRUGINFO

# Register your models here.

admin.site.register(MEMBERS)
admin.site.register(Search_History)
admin.site.register(DRUGINFO)