from django.contrib import admin
from .models import Operator


# Register your models here.
class OpAdmin(admin.ModelAdmin):
    search_fields = ['oper_id']


admin.site.register(Operator, OpAdmin)

