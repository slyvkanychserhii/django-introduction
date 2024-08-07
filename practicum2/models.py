from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.functions import Lower


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField('ProjectFile', related_name='projects')

    @property
    def count_of_files(self):
        return self.files.count()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        constraints = [
            models.UniqueConstraint(Lower('name'), 'created_at',  name='%(app_label)s_%(class)s_name_created_at_unique'),
        ]


StatusType = models.TextChoices('StatusType', 'NEW IN_PROGRESS COMPLETED CLOSED PENDING BLOCKED')
PriorityType = models.TextChoices('PriorityType', 'LOW MEDIUM HIGH VERY_HIGH')


class Task(models.Model):
    title = models.CharField(validators=[MaxValueValidator(10)], unique=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=15,
        choices=StatusType.choices,
        default=StatusType.NEW,
    )
    priority = models.CharField(
        max_length=15,
        choices=PriorityType.choices,
        default=PriorityType.LOW,
    )
    project = models.ForeignKey(to='Project', on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(to='Tag', null=True, blank=True, related_name='tasks')
    due_date = models.DateTimeField(null=True, blank=True)
    assignee = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-due_date', 'assignee']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        constraints = [
            models.UniqueConstraint(Lower('title'), 'project',  name='%(app_label)s_%(class)s_title_project_unique'),
        ]


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ProjectFile(models.Model):
    name = models.CharField(max_length=120)
    file = models.FileField(upload_to='project_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ProjectFile'
        verbose_name_plural = 'ProjectFiles'

