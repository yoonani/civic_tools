from django.contrib import admin

# Register your models here.
from .models import Question


# 관리자 페이지엣
admin.site.register(Question)