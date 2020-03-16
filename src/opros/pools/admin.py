from django.contrib import admin
from .models import Pool, Question, Answer


class PoolAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'deleted')
    #  list_filter = ('title',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'deleted')
    list_filter = ('pool',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'deleted')
    list_filter = ('question',)


admin.site.register(Pool, PoolAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
