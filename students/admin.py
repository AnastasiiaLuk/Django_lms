from django.contrib import admin
from students.models import Student

class GroupListFilter(admin.SimpleListFilter):
    from groups.models import Group
    title = 'group'
    parameter_name = 'group_filter'

    def lookups(self, request, model_admin):
        groups = self.Group.objects.all()
        data = [(group.pk, group.group_name) for group in groups]
        data.insert(0, (0, '-----'))
        return tuple(data)

    def queryset(self, request, queryset):
        value =  self.value()
        if value == None:
            return Student.objects.all()
        elif value == '0':
            return Student.objects.filter(group__isnull=True)
        else:
            return Student.objects.filter(group=self.Group.objects.get(pk=int(self.value())))


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_group_info')
    list_display_links = ('first_name', 'last_name', 'get_group_info')
    list_per_page = 17
    # list_filter = ('group__group_name',)
    list_filter = (GroupListFilter,)
    search_fields = ('first_name', 'last_name')

    def get_group_info(self, instance):
        if instance.group:
            return instance.group.group_name
        else:
            return ''

    def get_age(self, instance):
        return instance.get_age()

    readonly_fields = ('get_age',)
    get_group_info.short_description = 'group'
    get_age.short_description = 'Age'
    # fields = (
    #     ('first_name', 'last_name'),
    #     ('birthday', 'get_age'),
    #     ('email', 'phone'),
    #     'city',
    #     'group'
    # )

    fieldsets = (
        ('Personal info', {'fields': (('first_name', 'last_name'),)}),
        ('Born', {'fields': (('birthday', 'get_age'),)}),
        ('Contact info', {'fields': (('email', 'phone'),)}),
        ('  ', {'fields': ('city', 'group')})
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['group'].widget.can_add_related = False
        form.base_fields['group'].widget.can_change_related = False
        form.base_fields['group'].widget.can_view_related = False
        form.base_fields['group'].widget.can_delete_related = False

        return form


admin.site.register(Student, StudentAdmin)
