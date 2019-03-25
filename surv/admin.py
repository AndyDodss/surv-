from django.contrib import admin

# Register your models here.
from .models import Ask,Ans

admin.site.register(Ask)
admin.site.register(Ans)