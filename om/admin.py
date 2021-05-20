from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import TabularInline
from django.db import models
from .models import Home, About, Portfolio, Category, Skills, Profile

# Register your models here.

# Home
admin.site.register(Home)



# About
class ProfileInLine(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines= [
        ProfileInLine,
    ]
    

# Skills
class SkillsInLine(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInLine,
    ]

# Portfolio
admin.site.register(Portfolio) 