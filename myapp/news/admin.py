from django.contrib import admin
from news.models import Anchor
# Register your models here.
class AnchorAdmin(admin.ModelAdmin):
    list_display=('id','aid','name','email','phone')
admin.site.register(Anchor,AnchorAdmin)
