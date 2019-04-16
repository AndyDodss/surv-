from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Ask)
admin.site.register(Ans)
admin.site.register(Waiters)
admin.site.register(Branch)
admin.site.register(Source)