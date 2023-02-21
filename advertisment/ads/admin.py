from django.contrib import admin

from .models import Ads, Rubric


class AdsAdmin(admin.ModelAdmin):  # добавляем в админ-панель возможность поиска и изменяем визуал
    list_display = ('title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Ads, AdsAdmin)  # регистрируем модели в панели
admin.site.register(Rubric, RubricAdmin)
