from django.contrib import admin
from .models import Category, Question, Attempt

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Attempt)
