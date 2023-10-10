from django.contrib import admin
from . models import MemberTable, ContactTable, YogaTable, DiseaseTable

# Register your models here.
@admin.register(MemberTable)
class MemberTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email', 'mobile', 'pass1', 'disease')

@admin.register(YogaTable)
class YogaTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'disease_code', 'name')

@admin.register(ContactTable)
class ContactTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')

@admin.register(DiseaseTable)
class DiseaseTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'd_code', 'd_name')

# admin.site.register(MemberTable)
# admin.site.register(YogaTable)
# admin.site.register(ContactTable)
# admin.site.register(DiseaseTable)