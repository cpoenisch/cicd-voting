from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Administration Dashboard"
admin.site.site_title = "Administration Area"
admin.site.index_title = "CI/CD Systems"

# Using TabularInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),\
                 ('Date Information', {'fields': ['pub_date'],
                                       'classes':['collapse']}), ] # Don't forget to put "," at the on of the tupple
    # fieldsets = [(None, {'fields': ['question_text']}), ]
    inlines = [ChoiceInline]

# Register your models here to manage them from the admin page
admin.site.register(Question, QuestionAdmin)
