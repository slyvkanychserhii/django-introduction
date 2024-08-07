from django.contrib import admin
from .models import Project, Task, Tag, ProjectFile


def replace_spaces_to_underscores(self, request, objects):
    for obj in objects:
        obj.name = obj.name.replace(' ', '_')
        obj.save()
    return objects


replace_spaces_to_underscores.short_description = 'Replace spaces to underscores'


def update_status_to_close(self, request, objects):
    for obj in objects:
        obj.status = 'CLOSED'
        obj.save()
    return objects


update_status_to_close.short_description = 'Update status to close'


def change_priority_to_low(self, request, objects):
    for obj in objects:
        obj.priority = 'Low'
        obj.save()
    return objects


def change_priority_to_medium(self, request, objects):
    for obj in objects:
        obj.priority = 'Medium'
        obj.save()
    return objects


def change_priority_to_high(self, request, objects):
    for obj in objects:
        obj.priority = 'High'
        obj.save()
    return objects


def change_priority_to_very_high(self, request, objects):
    for obj in objects:
        obj.priority = 'Very High'
        obj.save()
    return objects


change_priority_to_low.short_description = 'Mark as Low priority'
change_priority_to_medium.short_description = 'Mark as Medium priority'
change_priority_to_high.short_description = 'Mark as High priority'
change_priority_to_very_high.short_description = 'Mark as Very High priority'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_count_of_files',)
    search_fields = ('name',)
    actions = [replace_spaces_to_underscores,]

    def display_count_of_files(self, obj):
        return obj.count_of_files

    display_count_of_files.short_description = 'Count of project files'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assignee', 'project', 'status', 'priority', 'created_at', 'due_date',)
    search_fields = ('title',)
    list_filter = ('status', 'priority', 'project', 'created_at', 'due_date', 'assignee',)
    actions = [
        update_status_to_close,
        change_priority_to_low,
        change_priority_to_medium,
        change_priority_to_high,
        change_priority_to_very_high,
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'created_at',)
    search_fields = ('title',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
