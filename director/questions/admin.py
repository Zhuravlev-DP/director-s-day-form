from django.contrib import admin
from questions.models import Division, Enterprise, Question


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('title', 'division')
    list_filter = ('title', 'division')
    search_fields = ('title', 'division')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'enterprise', 'text', 'email')
    list_filter = ('enterprise',)
    search_fields = ('pub_date', 'enterprise', 'text', 'email')
