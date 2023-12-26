from django.contrib import admin
from account.models import Teacher
# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display=('id','tid','tname','temail')
      
admin.site.register(Teacher,TeacherAdmin)