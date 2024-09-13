from django.contrib import admin
from core.models import College, Student, Teacher

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['college_id', 'name', 'created_at', 'updated_at']
    search_fields = ['name', ]
admin.site.register(Student, StudentAdmin)
admin.site.register(College)
admin.site.register(Teacher)