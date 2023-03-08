from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'salary')
    list_display_links = ('first_name', 'last_name', 'salary')
    list_per_page = 17
    search_fields = ('first_name', 'last_name')

    def get_age(self, instance):
        return instance.get_age()

    readonly_fields = ('get_age',)
    get_age.short_description = 'Age'

    fieldsets = (
        ('Personal info', {'fields': (('first_name', 'last_name'),)}),
        ('Born', {'fields': (('birthday', 'get_age'),)}),
        ('Salary', {'fields': ('salary',)})
    )
