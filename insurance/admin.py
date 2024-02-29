from django.contrib import admin
from .models import Category, Policy, PolicyRecord, Question

admin.site.register(Category)
admin.site.register(Policy)
admin.site.register(PolicyRecord)
admin.site.register(Question)
