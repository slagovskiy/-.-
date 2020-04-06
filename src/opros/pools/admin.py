from django.contrib import admin
from .models import Pool, Question, Answer, UserAnswer


class PoolAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'deleted')
    #  list_filter = ('title',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'deleted')
    list_filter = ('pool',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'deleted')
    list_filter = ('question',)


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'answer')


admin.site.register(Pool, PoolAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)
