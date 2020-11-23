from django.contrib import admin
from .models import Answer, FormData

class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id','questionNumber', 'answer'
    )



class FormAdmin(admin.ModelAdmin):
    list_display = (
        'id','email','age','gender','weight','get_answer','mark'
    )

# Register your models here.
admin.site.register(FormData,FormAdmin)
admin.site.register(Answer, AnswerAdmin)